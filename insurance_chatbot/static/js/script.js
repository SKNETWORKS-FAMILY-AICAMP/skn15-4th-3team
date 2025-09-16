// CSRF 토큰을 가져오는 함수
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

// 파일명 표시를 업데이트하는 함수
document.getElementById('file-input').addEventListener('change', function(e) {
    const fileNameDisplay = document.getElementById('file-name-display');
    if (this.files.length > 0) {
        fileNameDisplay.textContent = `📎 ${this.files[0].name}`;
    } else {
        fileNameDisplay.textContent = '';
    }
});

// 질문 답변 AJAX 처리 (FormData 버전)
document.getElementById('qa-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const questionInput = document.getElementById('question-input');
    const question = questionInput.value.trim();
    
    if (!question) {
        alert('질문을 입력해주세요.');
        return;
    }

    const chatWindow = document.getElementById('chat-window-qa');
    const loading = document.getElementById('loading');
    const sendBtn = document.getElementById('send-btn');
    
    // 사용자 질문 표시
    chatWindow.innerHTML += `
        <div class="message-container user">
            <div class="message user-message">
                <div class="message-content">${question}</div>
            </div>
        </div>
    `;
    
    // 로딩 표시
    loading.style.display = 'flex';
    sendBtn.disabled = true;
    questionInput.disabled = true;
    
    try {
        const csrfToken = getCSRFToken();

        // FormData 생성 (파일 포함 가능)
        const formData = new FormData();
        formData.append("question", question);

        const fileInput = document.getElementById('file-input');
        if (fileInput.files.length > 0) {
            formData.append("file", fileInput.files[0]);
        }

        const response = await fetch(RAG_API_URL, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        });

        const data = await response.json();
        
        console.log('Response status:', response.status);
        console.log('Response data:', data);
        
        if (response.ok) {
            // 답변 표시 (마크다운 렌더링)
            const renderedAnswer = marked.parse(data.answer);
            chatWindow.innerHTML += `
                <div class="message bot-message">
                    <div class="message-content">${renderedAnswer}</div>
                </div>
            `;
        } else {
            chatWindow.innerHTML += `
                <div class="message error-message">
                    <div class="message-content">오류: ${data.error}</div>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error:', error);
        chatWindow.innerHTML += `
            <div class="message error-message">
                <div class="message-content">네트워크 오류: ${error.message}</div>
            </div>
        `;
    } finally {
        // 로딩 숨기기
        loading.style.display = 'none';
        sendBtn.disabled = false;
        questionInput.disabled = false;
        questionInput.value = '';
        
        // 스크롤 맨 아래로 이동
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});

// 페이지 네비게이션
document.addEventListener('DOMContentLoaded', function() {
    const navElements = document.querySelectorAll('.logo-area-link, .sidebar nav a, .feature-card');

    navElements.forEach(element => {
        element.addEventListener('click', function(e) {
            e.preventDefault(); 
            
            const targetId = this.getAttribute('href') || this.getAttribute('data-target');
            
            if (!targetId || !targetId.startsWith('#')) return;

            document.querySelectorAll('.content-page').forEach(page => {
                page.classList.remove('active');
            });
            
            const targetPage = document.querySelector(targetId);
            if (targetPage) {
                targetPage.classList.add('active');
            }

            document.querySelectorAll('.sidebar nav a').forEach(link => {
                link.classList.remove('active');
            });

            if (this.closest('.sidebar')) {
                this.classList.add('active');
            }
        });
    });
});

// textarea에서 Enter 키로 전송하고 Shift+Enter로 줄바꿈하기
document.getElementById('question-input').addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        document.getElementById('qa-form').dispatchEvent(new Event('submit'));
    }
});