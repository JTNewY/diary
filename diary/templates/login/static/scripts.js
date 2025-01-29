document.getElementById("login-btn").addEventListener("click", function () {
    const loginForm = document.querySelector(".login-form");
    const hiddenContent = document.querySelector(".hidden-content");

    console.log("loginForm:", loginForm); // 확인용 로그
    console.log("hiddenContent:", hiddenContent); // 확인용 로그

    if (loginForm && hiddenContent) {
        // 로그인 폼 숨기기
        loginForm.classList.add("hidden");

        // 변경된 콘텐츠 보이기
        hiddenContent.classList.add("active");
    } else {
        console.error("요소를 찾을 수 없습니다. HTML 구조를 확인하세요.");
    }
});
