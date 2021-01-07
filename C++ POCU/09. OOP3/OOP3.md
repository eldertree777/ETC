# 상속

- class Cat : public Animal
```cpp
    class Animal{
        public:
            Animal(int age);
        private:
            int age;
    }
    class Cat : public Animal{
        public:
            Cat(char *name, int age);
        private:
            char name;
    }

    Cat::Cat(char *name, int age) : Animal(age){
        size_t size = strlen(name)+1; // unsigned int로 변환
        mName = new char[size];
        strcpy(mName , name);
    }
```

## 파생 클래스의 접근제어자 

## 메모리 A <- B <- C 호출순서
- C 생성후
    1. A 생성
    2. B 생성
    3. C 생성
- C 삭제시
    4. C 삭제
    5. B 삭제
    6. A 삭제


# 다형성
- 멤버 함수도 메모리 어딘가 위치함
- 멤버함수는 컴파일시 딱한번만 메모리 할당
- 저수준에서는 전역함수와 그다지 다르지않음

## 오버라이딩
- 자식이 재작성하여 사용

### Java vs cpp
- java는 자동 동적바인딩 , 기본적으로 가상함수
- cpp는 기본적으로 정적바인딩

## 정적 바인딩 CPP

## 동적 바인딩
- Virtual void move()

## 가상함수 
- 자식클래스의 멤버함수가 언제나 호출됨
- 모든 가상멤버함수의 주소를 포함
- 가상테이블을 만듬
- 가상테이블 : 점프테이블, 룩업테이블

## 가상 소멸자
- virtual ~Animal(); 
- 없을시 메모리누수 발생
- 모든클래스의 소멸자마다 넣을것!!

## 다형성의 의미
- 같은 모양의 코드가 다른행위를 하는것을 나타냅니다.
- 오버로딩

## 부모함수 호출
```cpp
    class A{
        over(){}
    }

    class B : public A{
        over(){A::over();}
    }
```

## 다중상속
- 함수중복 : 클래스 특정하기 bob->Cat::talk()
- 다이아몬드문제 : class tiger : virtual public Animal

- 다중상속을 피하고 인터페이스를 사용하자!!

## 추상클래스 
- virtual void Speak() = 0;
- 파생클래스에서 반드시 구현해야함
- 순수가상함수를 가지고있는 베이스 클래스를 추상클래스라 함;

## 인터페이스
- 순수가상함수만 가지고있는 클래스

