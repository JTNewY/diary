# 1. 환경설정 및 프로젝트 생성

### 파이썬 설치

```bash
pip install django
```

## diary project 생성

```bash
 django-admin startproject diary
```

## Board 앱 생성

```bash
python manage.py startapp board
```

# 2. 파일 구조

1. diary⇒ 프로젝트 폴더
2. diary/docs ⇒ 문서 폴더 
3. diary/frontend⇒  디자인 폴더
4. diary/.conda ⇒ 가상환경
5. diary/board ⇒ (앱) board

```bash
board
ㄴ views.py 
ㄴ urls.py
ㄴ models.py
ㄴ admin.py
```

1. diary/diary ⇒ diary 설정 파일

```bash
diary
ㄴ urls.py
ㄴ settings.py
```