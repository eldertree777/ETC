# 새로운 기능
- bool 데이터형
- 참조
- 개체지향 프로그래밍

## bool 데이터형
- true
- false

- 0 : false , 0 이외는 true

## reference
- 포인터를 사용하는 좀더 안전한 방법
- call by reference

```cpp
    int number = 100;
    int& referece = number;

    void Swap(int& number1, int& number2){
        int temp = number1;
        number1 = number2;
        number2 = temp;
    }
```

- 참조는 null을 할수없다.
- 소유하지않은 메모리장소를 가리킬수 없음


# 표준코딩
- 매개변수명을 잘짓자
- 읽기전용 매개변수는 상수참조
- 출력결과용 매개변수는 포인터

- ??? c# typescript 설계자가 같다?!