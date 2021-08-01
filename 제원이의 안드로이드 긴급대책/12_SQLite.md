# SQLite

## ADB ( android Debug Bridge) 상태확인, DBMS제어
1. AVD 실행
2. C:\Users\elder\AppData\Local\Android\Sdk\platform-tools
3. cmd
4. adb devices
5. adb root
6. adb -s 기기명 shell
7. cd /data/data/패키지명
8. sqlite3 DB명

9. .table
10. .schema 테이블명
11. .header on
12. .mode column


## SQLite 동작 방식
- SQLiteOpenHelper
- SQLiteDatabase
- Cursor