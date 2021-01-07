# OOP2

## 복사 생성자
```cpp
    class Vector{
        public:
            Vector(const Vector& other);
        private:
            int mX;
            int mY;
    };

    Vector::Vector(const Vector& other) : mX(other.mX),mY(other.mY){}
```

- 같은 클래스에 속한 다른개체를 이용하여 새로운 개체를 초기화
- 암시적 복사 생성자 만듬
- 얕은복사(각 맴버의 값을 복사함 )
- 얕은복사의 Delete문제점 **

## 깊은 복사
```cpp
    ClassRecord::ClassRecord(const ClasttRecord& other) : mCount(other.mCount){
        mScores = new int[mCount];
        memcpy(mScores, other.mScores,mCount * sizeof(int));
    }
```
* void* memcpy(void* destination, const void* source, size_t num);

## char배열과 복사 생성자

## 함수 오버로딩


## 함수 오버라이딩


## 연산자 오버로딩
```cpp
    Vector operator+(const Vector& rhs) const;

    Vector Vector::operator+(const Vector& rhs) const{
        Vector sum;
        sum.mX = mX + rhs.mX;
        sum.mY = mY + rhs.mY;

        return sum;
    }
```

- v1 + v2
- V1.operator+(v2)

## friend 함수
- 다른 클래스나 함수가 나의 private, protected멤버에 접근할수있도록 허용

```cpp
    class X{
        friend void foo();
        friend class Y;
        private:
        public:
        
    }

    friend std::ostream& operator<<(std::ostream& os, const Vector& rhs){

        return os;
    }
```

## 전역함수로 연상자 오버로딩


## 연산자 오버로딩과 const
- 멤버변수의 값이 바뀌는것을 방지
- 최대한 많은곳에 const를 붙일것!

### const& 를 사용하는 이유
- 불필요한 개체의 사본이 생기는것 방지
- 멤버 변수가 반뀌는 것도 방지

## 연산자 오버로딩을 남용하지말라!

## 대입연산자
- 복사 생성자와 거의 동일
- 암시적으로 operator= 구현해줌

## 암시적 함수들을 제거하는법
- 전통적인 방법
    - 매개변수없는 생성자
    - 복사 생성자
    - 소멸자
    - 대입연산자
```cpp
    class Vector{
        public:
        private:
            Vector(){}; // 1. 기본생성자 지우기
             Vector(const Vector& other); //2. 복사생성자 지우기
             ~Vector(){}; //3. 소멸자 지우기
             const Vector& operator=(const Vector& rhs); //4. 대입연산자 지우기
    }
```

