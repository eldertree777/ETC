# chapter 1
## 인터넷과 프로토콜 소개

- 인터넷
> - 다양한 어플리케이션에 통신서비스를 제공하는 인프라(웹,게임)
> - 어플리케이션 통신관련 프로그래밍 인터페이스 제공 (API, Protocol)
> - 각 장치들은 다양한 총신 링크를 통해 연결, 링크를 통해 패킷단위 데이터 전달
> - 네트워크의 네트워크 : ISP의 집합, 패킷전송을 위해 프로토콜과 인터넷 표준사용(TCP/IP)

* RJ45 - 랜선
* 종단시스템 = 통신링크 + 패킷스위치

- 1계층
> 전국 or 국가간 네트워크 운영 (KT, NTT,...)

- CP
> 자신의 data center- Internet 사설네트워크 구성 (google)

- router 
> 가장 안정적인 유선링크 

- ISP
> 인터넷 서비스 공급자 망관리자 (라우터 스위치 관리)

- 프로토콜
> 네트워크 구성요소간 주고받는 메세지 형식과 순서 (Sender - Reciever 규약)
> 송수신시 동작도 규정(HTTP, TCP/IP, UDP)

## 네트워크 구성

- 네트워크 엣지 : host이며, ISP에 의한 인터넷 연결
- 엑세스 네트워크 : 유,무선 통신링크
- 네트워크 코어 : 다수의 라우터의 연결, 네트워크의 네트워크 (화웨이)

- 네트워크 엣지

> 엑세스 네트워크에 연결된 host

> 대역폭 : bandwidth bps(bit per secound)

> 공유 or 단곧 사용 미디어?

- 네트워크 코어 : 라우터들의 집합, 라우터 사이 패킷교환
> 기능 -> 라우팅 : 송신지 -> 목적지 전달 경로 탐색

> 포워딩 : 적절한 출력 링크로 내보내기 ( 패킷교환, 회선교환 )

- 패킷교환 : 응용계층에서 데이터를 패킷으로 자르고 전송
> store and forward : 패킷하나를 저장후 전송

> end to end delay : 지연 발생

> 큐잉 : 패킷들이 하나의 저장소 보관

> loss :  패킷도착율 > 전송율 (오버플로우 발생) 패킷지연

- 패킷지연 4가지 요소
> 처리 지연 : 비트에러체크, 출력 링크 결정

> 큐잉 지연 : 출력링크로 전송되기까지 큐에서 기다리는 시간

> 전송 지연 : 노드 -> 링크 (링크로 내보내는 시간)

> 전파 지연 : 링크 (다음 목적지 도착)

- 회선교환 : 종단간 예약되어 자원 할당 ( 자원의 단독 사용 )
> 품질보장 , 자원낭비
> FDM : 주파수 분할
> TDM : 시분할

- 패킷교환 vs 회선교환
> 패킷교환이 사용자수가 더많이 사용가능
> but 혼잡상태 발생 , 신뢰성, 혼잡제어 프로토콜 필요
> 즉 대여폭 보장 필요

- 네트워크 처리율 bit / secound (bps)

##  네트워크 계층화와 모델링
- OSI 7 Layer
    - Application : ftp,smtp, http
    - presentation : 암호화, 압축
    - session : 동기화 , 체크포인트 , 교환 메세지 회복
    - Transport : p-p (TCP, UDP)
    - Network : 데이터그램(패킷) 라우팅 (IP/ 라우팅 프로토콜)
    - Link : 이더넷, Wifi
    - physical : 물리매체를 통해 bit 전달

- 계층화의 장점 : 복잡한 시스템 단순화 (유지보수 비용 감소)
- 캡슐화

# Chaper2
## 네트워크 어플리케이션 소개
- network application : host에서 동작 end to end
    - 네트워크 코어 장치를 위한 코드 작성 x
    - 분류 : C-S , P2P

- Client- Server
    - Client : 서버와 통신을 통해 필요한 기능 수행
    - Server : Always-on, 고정 IP (데이터 센터)

- P2P
    - 항상 동작하는 서버 x , 임의 단말과 직접통신
    - 자기 확장성 : 각각의 피어는 이용자이면서 제공자 이기도함
    - but : 보안, 성능, 관리가 어려움 (신뢰성 떨어짐)

- process : host 에서 동작하는 프로그램
    - IPC : 단일 호스트에서 프로세스간 통신
    - 메세지 교환 : 다른 host 끼리 프로세스간 통신 (socket)

- Socket : 각 프로세스는 소켓을 이용해 메세지 수신
    - A - T 인터페이스

- 프로세스간 메세지 전달을 위해서 식별자 (IP + Port) 필요

- Application Protocol
    - 메세지종류( request, respond, etc)
    - 구문, 의미, 전송 규칙

- open protocol
    - IETF RFC
    - 상호 연동성 제공 
    - http , smtp

- 비공개 프로토콜
    - skype


- Transport Layer Protocol for Application Layer
    - 데이터 무결성 (신뢰성)
    - 처리율 대여폭 증가
    - 타이밍 낮은 delay 도구
    - 보안 암호화/복호화 데이터 무결성

- TCP : 실시간 하락, 최소 처리율 보장 x , 보안 x
    - 연결지향형 서비스
    - 플로우제어, 혼잡제어, 연결지향

* TCP + 보안 -> SSL -> TLS

- UDP : 신뢰성 x, 플로우제어 x , 혼잡제어x, 연결설립 x, 실시간
- TCP + UDP는 보안 x 암호화 절차가 없다.

## web, http and protocol
- webpage : 다수의 object로 구성

