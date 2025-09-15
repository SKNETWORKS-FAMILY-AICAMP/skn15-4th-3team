// --- 기본 요소 변수 선언 ---
const navLinks = document.querySelectorAll('.nav-link');
const contentPages = document.querySelectorAll('.content-page');
const sidebar = document.getElementById('sidebar');
const sidebarToggleBtn = document.getElementById('sidebar-toggle-btn');
const featureCards = document.querySelectorAll('.feature-card');
const recentChatsList = document.getElementById('recent-chats-list');
const qaChatWindow = document.getElementById('chat-window-qa');
const askButton = document.getElementById('ask-button');
const questionInput = document.getElementById('question-input');
const recommendChatWindow = document.getElementById('chat-window-recommend');
const recommendButton = document.getElementById('recommend-button');

// --- 페이지 전환 로직 ---
function switchPage(targetId) {
    contentPages.forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    const targetPage = document.querySelector(targetId);
    const activeLinks = document.querySelectorAll(`a[href="${targetId}"]`);
    if (targetPage) targetPage.classList.add('active');
    activeLinks.forEach(l => l.classList.add('active'));
}

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        switchPage(targetId);
        window.location.hash = targetId;
    });
});

// --- 사이드바 접기 기능 로직 ---
sidebarToggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
});

// --- 홈페이지 카드 클릭 로직 ---
featureCards.forEach(card => {
    card.addEventListener('click', () => {
        const targetId = card.getAttribute('data-target');
        switchPage(targetId);
        window.location.hash = targetId;
    });
});

// --- 최근 채팅 기록 로직 ---
function addChatToHistory(summary, targetPageId) {
    for (let item of recentChatsList.children) {
        if (item.textContent === summary) return;
    }
    const listItem = document.createElement('li');
    const link = document.createElement('a');
    link.href = targetPageId;
    link.textContent = summary;
    link.classList.add('nav-link');
    link.addEventListener('click', (e) => {
         e.preventDefault();
         switchPage(targetPageId);
         window.location.hash = targetPageId;
    });
    listItem.appendChild(link);
    recentChatsList.prepend(listItem);
}

// --- 공용 채팅 메시지 추가 함수 ---
function appendMessage(chatWindow, message, type) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', `${type}-message`);
    messageElement.innerText = message;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

// --- 질문 답변(QA) 페이지 기능 로직 (마크다운 렌더링 + 스크롤 포함) ---
askButton.addEventListener('click', async () => {
    const question = questionInput.value.trim();
    if (question === '') return;

    // 첫 질문이면 최근 채팅 기록에 추가
    if (qaChatWindow.children.length === 0) {
        addChatToHistory(question, '#qa-page');
    }

    // 사용자 질문 화면에 추가
    appendMessage(qaChatWindow, question, 'user');
    questionInput.value = '';

    try {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        const response = await fetch("/rag_view/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({ "question": question })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // AI 답변 마크다운 렌더링 후 추가
        appendMessage(qaChatWindow, data.answer, 'ai');

    } catch (error) {
        console.error('Error:', error);
        appendMessage(qaChatWindow, '죄송합니다. 답변을 가져오는 중 오류가 발생했습니다.', 'ai');
    }
});

// --- appendMessage 함수 수정: 마크다운 렌더링 포함 ---
function appendMessage(chatWindow, message, type) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', `${type}-message`);

    if (type === 'ai') {
        // 마크다운 렌더링 (marked 라이브러리 필요)
        messageElement.innerHTML = marked.parse(message);
    } else {
        messageElement.innerText = message;
    }

    chatWindow.appendChild(messageElement);
    // 항상 최신 메시지로 스크롤
    chatWindow.scrollTop = chatWindow.scrollHeight;
}


// --- 정보 추천 페이지 기능 로직 ---
recommendButton.addEventListener('click', () => {
    // ## 수정된 부분: 라디오 버튼 미선택 시 오류 방지 ##
    const checkedGender = document.querySelector('input[name="gender"]:checked');
    if (!checkedGender) {
        alert('성별을 선택해주세요!');
        return;
    }
    const gender = checkedGender.value;
    const age = document.getElementById('age-input').value;
    const carType = document.getElementById('car-type-select').value;
    if (age === '') { alert('나이를 입력해주세요!'); return; }
    
    const userRequest = `성별: ${gender}, 나이: ${age}세, 관심 차종: ${carType}에 대한 추천을 원합니다.`;
    if (recommendChatWindow.children.length === 0) {
        addChatToHistory(`추천: ${carType}`, '#recommend-page');
    }
    appendMessage(recommendChatWindow, userRequest, 'user');
    
    // 이 부분도 나중에 서버와 연동할 수 있습니다.
    setTimeout(() => {
        const aiRecommendation = `${gender}, ${age}세를 위한 ${carType} 차량 추천 결과입니다. AI가 생성한 추천 내용을 여기에 표시합니다.`;
        appendMessage(recommendChatWindow, aiRecommendation, 'ai');
    }, 500);
});

// --- 초기 페이지 설정 로직 ---
const initialHash = window.location.hash || '#home-page';
switchPage(initialHash);