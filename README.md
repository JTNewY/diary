```markdown

# Django 프로젝트 구조 및 환경설정

## 1. Django 설치 및 프로젝트 생성
### 파이썬 패키지 설치
Django를 설치하려면 다음 명령어를 실행합니다.
```bash
pip install django

```

### 프로젝트 생성

`diary`라는 이름의 프로젝트를 생성합니다.

```bash

django-admin startproject diary
```

### Board 앱 생성

프로젝트 내에서 `board`라는 앱을 추가합니다.

```bash

python manage.py startapp board

```

---

## 2. 파일 및 폴더 구조

### (1) **프로젝트 폴더: `diary`**

- Django 프로젝트의 최상위 폴더로, 전체 프로젝트의 설정과 환경을 관리합니다.

### (2) **문서 폴더: `diary/docs`**

- 프로젝트와 관련된 문서를 보관합니다.

### (3) **디자인 폴더: `diary/frontend`**

- HTML, CSS, JavaScript 등 프론트엔드 리소스를 관리하는 폴더입니다.

### (4) **가상환경 폴더: `diary/.conda`**

- Python 가상환경을 관리하는 폴더입니다.

### (5) **앱 폴더: `diary/board`**

`board` 앱의 주요 구성 파일:

- `views.py`: 요청(request)을 처리하고 응답(response)을 반환하는 함수/클래스를 정의합니다.
- `urls.py`: 앱의 URL 라우팅을 정의합니다.
- `models.py`: 데이터베이스 테이블 및 모델을 정의합니다.
- `admin.py`: Django Admin 인터페이스를 설정합니다.

### (6) **설정 파일 폴더: `diary/diary`**

프로젝트의 설정과 URL을 관리하는 핵심 폴더:

- `urls.py`: 프로젝트 전역 URL 라우팅 설정 파일.
- `settings.py`: 데이터베이스, 앱 등록, 미들웨어 등 프로젝트 설정 파일.

---

## 3. 전체 파일 구조

```
plaintext
코드 복사
diary/
├── docs/             # 문서 폴더
├── frontend/         # 프론트엔드 폴더
├── .conda/           # 가상환경 폴더
├── board/            # 앱 폴더
│   ├── views.py      # 요청과 응답 처리
│   ├── urls.py       # URL 라우팅
│   ├── models.py     # 데이터베이스 모델
│   ├── admin.py      # 관리자 설정
└── diary/            # 프로젝트 설정 폴더
    ├── urls.py       # 프로젝트 URL 설정
    ├── settings.py   # 프로젝트 환경 설정

```