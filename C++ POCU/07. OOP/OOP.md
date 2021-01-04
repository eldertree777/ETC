# OOP

## 접근제어자
- 맴버변수이름 mX,mY
- cpp 기본접근권한 private
- public
- private
- protected : 자식클래스에서 접근가능

## 개체 생성
- Vector a; : 스택메모리
- Vector* b = new Vector();

## 스택
- 예약된 로컬 메모리
- 함수 호출과 반환이 일어남

- 단순히 스택포인터를 옮김
    - 메모리 할당 및 헤제할 필요가 없음
    - 스택에 할당된 메모리는 범위를 벗어나면 사라짐
    - 변수와 매개변수를 위해 필요한 크기는 컴파일 도중에 알수있음
- 하지만 스택에 큰개체를 많이 넣으면
    - 스택오버플로우 발생
    - 성능이 느려짐

## 힙
- 전역 메모리 공간
- 비어있고 연속된 메모리 블록찾아야함
- 프로그래머가 직접 할당및 해제해야함 

## 개체배열
- Vector* list = new Vector[10]; // 자바에서는 포인터배열, cpp는 개체배열
- Vector** list = new Vector*[10];

## 개체소멸
- delete a;
- delete[] list;

## 맴버변수 초기화
- java나 c# 은 0으로 초기화
- cpp는 초기화 x

### new/delete vs malloc()/free()
- 생성자

## 생성자
```cpp
    Vector():mX(0),mY(0)
```

## 소멸자
```cpp
    ~Vector();
```

## const 맴버 함수
- int GetX() const; : 개체 안의 어떠한것도 바꾸지 않음

## 구조체 vs 클래스
- 기본 접근지정자
- 그외 똑같음