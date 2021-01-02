# File I/O
- ifstream : 파일 입력
- ofstream : 파일 출력
- fstream : 파일입력 및 출력
- 파일스트림에 <<, >>, 조정자등도 쓸수있음

## 파일열기
```cpp
    ifstream fin;
    fin.open("hello.txt");

    ofstream fout;
    fout.open("hello.txt")

    fstream fs;
    fs.open("hello.txt");
```

- fin.open("HelloWorld.txt", ios_base::in | ios_base::binary);  : 끝에 비트플래그를 넣을수 있다
- 모드 플래그 ios_base

## 파일 닫기
- fin.close();

## 스트림 상태 확인하기
- if(fs.is_open()){}

## 파일에서 문자 하나씩 읽기
```cpp
    while(true){
        if(fin.fail()){
            break;
        }
        cout << character;
    }
```

## 파일에서 문자 한줄씩 읽기
```cpp
    while(true){
        if(!fin.eof()){
            getline(fin, line);
            cout << line << endl;
        }
    }
```
## 빈파일 읽기

## 파일에서 한단어씩읽기
```cpp
    while(!fin.eof()){
        fin>>name >>balance;
        cout << name << ": $" << balance << endl;
    }
    // >> 은 스페이스까지 읽는다
```
## 잘못된 파일 읽기
- fin.clear() : badbit clear
- fin.ignore(LLONG_MAX, ' ');

- failbit
- eofbit 주의!

## 기억하자
- 입출력 연산이 스트림 상태 비트를 변경
- EOF 잘못 처리시 무한루프
- clear() 사용시 위치 생각

## 베스트 프렉티스
- 입출력 처리는 업계에서 매우 흔한 문제
- 자신만의 스트림 리더를 만드는일이 흔함

### best testcase


## 파일에 쓰기
```cpp
    if(!cin.fail()){
        fout<<line<<endl;
        }
```

- put()
- <<

## 바이너리 파일 읽기
```cpp
    ifstream fin("..txt",ios_base::in |ios_base::binary);

    if(fin.is_open()){
        Record record; //char[20] * 2 + int * 1
        fin.read((char*)&record, sizeof(Record));
    }

    fin.close();
```

- read(char* , streamsize)
- fin.read(&firstName , 20) : 파일로부터 문자 20자를 읽어 firstname에 저장

## 바이너리 파일 쓰기
```cpp
    if(fout.is_open()){
        char buffer[20] = "hello wordl";
        fout.write(buffer,20);
    }
```

- write(const char*, size)

## 파일안에서의 탐색
```cpp
     if(fout.is_open()){
         fs.seekp(20, ios_base::beg);
         if(!fs.fail()){
             // 21번째 위치에서부터 덮어쓰기
         }
    }
```

### 탐색 유형
- 절대적
    - 특정위치로 감
    - tellp/tellg
- 상대적
    - beg
    - cur
    - end

- tellp() : 쓰기 포인터의 위치를구함
    - ios::pos_type pos = fout.tellp();

- seekp()
    - fout.seekp(0) : 처음위치로 이동
    - fout.seekp(20, ios_base::cur); : 현재위치로부터 20바이트 뒤로

- tellg() : 읽기 포인터의 위치 구함