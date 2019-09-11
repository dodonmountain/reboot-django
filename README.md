# Django

## Model 정의

* title: `charfield` maxlength 30
* content: textfield
* created_at: auto_now_add, datetime
* updated_at: auto_now

## CRUD

* C
  * `/new/`: 글 작성 form
  * `/create/`: 저장 후 index로 보내기(redirect)
* R
  * `/1/`
* U
  * `1/delete/`: 삭제 후 index로 보내기
* D
  * `/1/edit/`:글 수정 form
  * `/1/update/`: 저장 후 Read로 보내기
* 