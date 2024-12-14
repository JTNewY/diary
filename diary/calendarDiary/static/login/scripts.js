// 로그인 시행하면 loginForm > mypage 변경
document.getElementById("login-btn").addEventListener("click", function () {
    const loginForm = document.querySelector(".login-form");
    const mypage = document.querySelector(".hidden-content");

    console.log("loginForm:", loginForm); // 확인용 로그
    console.log("mypage:", mypage); // 확인용 로그

    if (loginForm && mypage) {
        // 로그인 폼 숨기기
        loginForm.classList.add("hidden");

        // 변경된 콘텐츠 보이기
        mypage.classList.add("active");
    } else {
        console.error("요소를 찾을 수 없습니다. HTML 구조를 확인하세요.");
    }
});

// Sing up 눌렸을 때
document.getElementById("Sign-up").addEventListener("click", function () {
    const loginForm = document.querySelector(".login-form");
    const mypage = document.querySelector(".hidden-content");

    console.log("loginForm:", loginForm); // 확인용 로그
    console.log("mypage:", mypage); // 확인용 로그

    if (loginForm && mypage) {
        // 로그인 폼 숨기기
        loginForm.classList.add("hidden");

        // 변경된 콘텐츠 보이기
        mypage.classList.add("active");
    } else {
        console.error("요소를 찾을 수 없습니다. HTML 구조를 확인하세요.");
    }
});

// 로그인 시행하면 loginForm > mypage 변경
document.getElementById("Find-ID").addEventListener("click", function () {
    const loginForm = document.querySelector(".login-form");
    const mypage = document.querySelector(".hidden-content");

    console.log("loginForm:", loginForm); // 확인용 로그
    console.log("mypage:", mypage); // 확인용 로그

    if (loginForm && mypage) {
        // 로그인 폼 숨기기
        loginForm.classList.add("hidden");

        // 변경된 콘텐츠 보이기
        mypage.classList.add("active");
    } else {
        console.error("요소를 찾을 수 없습니다. HTML 구조를 확인하세요.");
    }
});

// 로그인 시행하면 loginForm > mypage 변경
document.getElementById("Find-PW").addEventListener("click", function () {
    const loginForm = document.querySelector(".login-form");
    const mypage = document.querySelector(".hidden-content");

    console.log("loginForm:", loginForm); // 확인용 로그
    console.log("mypage:", mypage); // 확인용 로그

    if (loginForm && mypage) {
        // 로그인 폼 숨기기
        loginForm.classList.add("hidden");

        // 변경된 콘텐츠 보이기
        mypage.classList.add("active");
    } else {
        console.error("요소를 찾을 수 없습니다. HTML 구조를 확인하세요.");
    }
});