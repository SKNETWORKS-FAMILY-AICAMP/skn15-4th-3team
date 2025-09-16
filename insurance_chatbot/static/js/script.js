document.addEventListener('DOMContentLoaded', function() {
    // 1. DOM 요소
    const contentPages = document.querySelectorAll('.content-page');
    const navLinks = document.querySelectorAll('.nav-link');
    const featureCards = document.querySelectorAll('.feature-card');
    const sidebar = document.getElementById('sidebar');
    const sidebarToggleBtn = document.getElementById('sidebar-toggle-btn');
    const chatWindow = document.getElementById('chat-window-qa');
    const qaForm = document.getElementById('qa-form');
    const questionInput = document.getElementById('question-input');
    const fileInput = document.getElementById('file-input');
    const fileNameDisplay = document.getElementById('file-name-display');
    const loading = document.getElementById('loading');
    const sendBtn = document.getElementById('send-btn');
    const newChatBtn = document.getElementById('new-chat-btn');
    const recentChatsList = document.getElementById('recent-chats-list');

    // --- 추천 페이지 관련 DOM 요소 추가 ---
    const recommendButton = document.getElementById('recommend-button');
    const recommendChatWindow = document.getElementById('chat-window-recommend');
    const ageInput = document.getElementById('age-input');
    const carTypeSelect = document.getElementById('car-type-select');
    // --- 추가 끝 ---

    // 2. 상태 관리
    let chatHistory = [];
    let currentChatId = null;

    // 3. 페이지 전환 로직
    function switchPage(targetId) {
        contentPages.forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        const targetPage = document.querySelector(targetId);
        const activeLinks = document.querySelectorAll(`a[href="${targetId}"]`);
        if (targetPage) targetPage.classList.add('active');
        activeLinks.forEach(l => l.classList.add('active'));
    }

    // 4. 채팅 기록 관리 로직
    function saveHistory() { localStorage.setItem('chatHistory', JSON.stringify(chatHistory)); }
    function renderSidebar() {
        recentChatsList.innerHTML = '';
        if (!chatHistory || chatHistory.length === 0) return;
        chatHistory.forEach(chat => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = '#';
            a.textContent = chat.title;
            a.dataset.chatId = chat.id;
            li.appendChild(a);
            recentChatsList.appendChild(li);
        });
    }
    function loadChat(chatId) {
        const chat = chatHistory.find(c => c.id === chatId);
        if (!chat) return;
        currentChatId = chatId;
        chatWindow.innerHTML = ''; 
        chat.messages.forEach(msg => addMessageToWindow(msg.sender, msg.content, msg.sender === 'ai'));
        switchPage('#qa-page');
    }
    function startNewChat() {
        currentChatId = null;
        chatWindow.innerHTML = `<div class="welcome-message"><p>안녕하세요! 운전자 보험에 대해 궁금한 점을 질문해주세요.</p></div>`;
        questionInput.value = '';
        fileInput.value = '';
        fileNameDisplay.textContent = '';
        switchPage('#qa-page');
    }
    function addMessageToWindow(sender, content, isHtml = false) {
        const container = document.createElement('div');
        container.className = `message-container ${sender}`;
        const avatar = document.createElement('div');
        avatar.className = 'avatar';
        avatar.textContent = sender === 'user' ? '👤' : '🤖';
        const message = document.createElement('div');
        message.className = `message ${sender}-message`;
        if (isHtml) message.innerHTML = content;
        else message.textContent = content;
        container.append(avatar, message);
        chatWindow.appendChild(container);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // 5. 이벤트 핸들러
    async function handleFormSubmit(e) {
        e.preventDefault();
        const question = questionInput.value.trim();
        if (!question) return alert('질문을 입력해주세요.');

        if (currentChatId === null) chatWindow.innerHTML = '';
        
        addMessageToWindow('user', question);
        loading.style.display = 'flex';
        sendBtn.disabled = true;
        
        let newChatCreated = false;
        if (currentChatId === null) {
            currentChatId = Date.now();
            const newChat = {
                id: currentChatId,
                title: question.substring(0, 20) + (question.length > 20 ? '...' : ''),
                messages: [{ sender: 'user', content: question }]
            };
            chatHistory.unshift(newChat);
            newChatCreated = true;
        } else {
            chatHistory.find(c => c.id === currentChatId).messages.push({ sender: 'user', content: question });
        }

        const formData = new FormData(qaForm);
        const csrfToken = qaForm.querySelector('[name=csrfmiddlewaretoken]').value;
        
        try {
            const response = await fetch(RAG_API_URL, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrfToken },
                body: formData
            });
            const data = await response.json();
            
            const answer = response.ok ? marked.parse(data.answer) : `오류: ${data.error}`;
            addMessageToWindow('ai', answer, true);
            chatHistory.find(c => c.id === currentChatId).messages.push({ sender: 'ai', content: answer });

        } catch (error) {
            addMessageToWindow('ai', `네트워크 오류: ${error.message}`, true);
        } finally {
            loading.style.display = 'none';
            sendBtn.disabled = false;
            questionInput.value = '';
            fileInput.value = '';
            fileNameDisplay.textContent = '';
            saveHistory();
            if (newChatCreated) renderSidebar();
        }
    }

    // --- LLM 기반 보험 추천 핸들러 추가 ---
    async function handleRecommendationSubmit() {
        const genderInput = document.querySelector('input[name="gender"]:checked');
        const age = ageInput.value;
        const carType = carTypeSelect.value;
        
        if (!age) {
            alert('나이를 입력해주세요!');
            ageInput.focus();
            return;
        }
        if (!genderInput) {
            alert('성별을 선택해주세요!');
            return;
        }

        const genderText = genderInput.value === 'male' ? '남성' : '여성';
        const carTypeText = carTypeSelect.options[carTypeSelect.selectedIndex].text;

        const prompt = `
            당신은 친절하고 전문적인 자동차 보험 전문가입니다. 
            아래 사용자 정보를 바탕으로 가장 적합한 가상의 자동차 보험 상품을 추천해주세요.
            왜 그 상품을 추천하는지 이유를 쉽고 명확하게 설명하고, Markdown을 사용해서 강조해주세요.

            - **나이**: ${age}세
            - **성별**: ${genderText}
            - **차종**: ${carTypeText}

            답변은 반드시 한국어로 생성해주세요.
        `;

        try {
            recommendButton.disabled = true;
            recommendButton.textContent = 'AI 분석 중...';
            recommendChatWindow.innerHTML = `<div class="loading-spinner"></div>`;

            const response = await fetch(RAG_API_URL, { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': qaForm.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify({
                    question: prompt
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || '서버에서 오류가 발생했습니다.');
            }

            const data = await response.json();
            const recommendationHtml = marked.parse(data.answer); 

            recommendChatWindow.innerHTML = `<div class="message bot-message">${recommendationHtml}</div>`;

        } catch (error) {
            recommendChatWindow.innerHTML = `<div class="message bot-message error">죄송합니다. 추천 정보를 가져오는 중 오류가 발생했습니다: ${error.message}</div>`;
        } finally {
            recommendButton.disabled = false;
            recommendButton.textContent = '추천받기';
        }
    }
    // --- 추가 끝 ---

    // 6. 이벤트 리스너 등록
    qaForm.addEventListener('submit', handleFormSubmit);
    newChatBtn.addEventListener('click', (e) => { e.preventDefault(); startNewChat(); });
    sidebarToggleBtn.addEventListener('click', () => sidebar.classList.toggle('collapsed'));
    
    // --- 추천 버튼 이벤트 리스너 추가 ---
    recommendButton.addEventListener('click', handleRecommendationSubmit);
    // --- 추가 끝 ---
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href');
            if (targetId && targetId.startsWith('#')) {
                e.preventDefault();
                switchPage(targetId);
            }
        });
    });
    featureCards.forEach(card => card.addEventListener('click', () => switchPage(card.getAttribute('data-target'))));
    recentChatsList.addEventListener('click', (e) => {
        if (e.target.tagName === 'A') {
            e.preventDefault();
            loadChat(Number(e.target.dataset.chatId));
        }
    });
    fileInput.addEventListener('change', () => {
        fileNameDisplay.textContent = fileInput.files.length > 0 ? `첨부: ${fileInput.files[0].name}` : '';
    });

    // 7. 초기화
    function init() {
        const savedHistory = localStorage.getItem('chatHistory');
        if (savedHistory) chatHistory = JSON.parse(savedHistory);
        renderSidebar();
        
        const initialHash = window.location.hash || '#home-page';
        switchPage(initialHash);
    }

    init();
});