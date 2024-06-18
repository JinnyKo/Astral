# Astral 


## 준비물 
1. 갤럭시 S20 스마트폰
2. USB 케이블: 스마트폰과 컴퓨터를 연결하기 위한 케이블
3. 컴퓨터: 개발 환경을 설정하고 모델을 스마트폰으로 전송하기 위한 컴퓨터
4. Android Studio: 안드로이드 개발을 위한 IDE
5. ADB (Android Debug Bridge): 스마트폰과의 통신을 위한 툴
6. TensorFlow Lite 모델 파일: 경량화된 모델 파일 (.tflite)

## 단계별 과정
1. 개발 환경 설정
Android Studio 설치 및 설정

Android Studio 를 다운로드하여 설치합니다.
ADB 설치

ADB는 Android Studio와 함께 설치되지만, 필요시 별도로 설치할 수 있습니다.
2. TensorFlow Lite 모델 준비
경량화된 모델 파일 (.tflite)을 준비합니다. 예를 들어, model.tflite 파일을 준비합니다.

3. 스마트폰과 컴퓨터 연결
USB 디버깅 활성화

스마트폰에서 설정 > 개발자 옵션으로 이동하여 USB 디버깅을 활성화합니다.
개발자 옵션이 보이지 않는 경우, 설정 > 휴대전화 정보 > 소프트웨어 정보로 이동하여 빌드 번호를 여러 번 탭하여 개발자 옵션을 활성화합니다.
USB 케이블 연결

USB 케이블을 사용하여 갤럭시 S20 스마트폰을 컴퓨터에 연결합니다.
ADB 연결 확인

터미널(또는 명령 프롬프트)에서 다음 명령을 실행하여 스마트폰이 ADB에 연결되었는지 확인합니다.
bash
코드 복사
adb devices
연결된 디바이스 목록에 스마트폰이 표시되어야 합니다.
4. 모델 파일을 스마트폰에 전송
모델 파일 전송
ADB를 사용하여 TensorFlow Lite 모델 파일을 스마트폰의 내부 저장소로 전송합니다. 예를 들어, model.tflite 파일을 /sdcard/Download/ 디렉토리에 전송합니다.
bash
코드 복사
adb push path/to/model.tflite /sdcard/Download/
5. 안드로이드 앱에서 모델 파일 사용
안드로이드 앱 프로젝트 생성

Android Studio에서 새로운 안드로이드 프로젝트를 생성합니다.

델 파일 복사

앱 실행 시 모델 파일을 내부 저장소로 복사하도록 코드를 작성합니다.

```
import android.content.Context;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class ModelUtils {
    public static void copyModelToInternalStorage(Context context) throws IOException {
        File modelFile = new File(context.getFilesDir(), "model.tflite");
        if (!modelFile.exists()) {
            try (InputStream input = new FileInputStream(new File("/sdcard/Download/model.tflite"));
                 FileOutputStream output = new FileOutputStream(modelFile)) {
                byte[] buffer = new byte[1024];
                int length;
                while ((length = input.read(buffer)) > 0) {
                    output.write(buffer, 0, length);
                }
            }
        }
    }
}

```


## WORKFLOW
```
+-----------------------+-----------------------------------------+
| 단계                  | 작업                                    |
+-----------------------+-----------------------------------------+
| 1. 프로젝트 초기 설정 | - 프로젝트 목표 및 범위 정의             |
|                       | - 주요 마일스톤 설정                    |
|                       | - 요구 사항 분석                        |
|                       | - Git 리포지토리 생성                   |
|                       | - 프로젝트 구조 설정                    |
|                       | - README 파일 작성                      |
+-----------------------+-----------------------------------------+
| 2. 개발 환경 설정    | - Android Studio 설치                   |
|                       | - TensorFlow 및 TensorFlow Lite 설치    |
|                       | - ADB 및 Fastboot 설치                  |
|                       | - Android SDK 설치                      |
|                       | - Google Play Services 설치 (필요 시)   |
+-----------------------+-----------------------------------------+
| 3. 모델 준비         | - LLM 모델 선택 및 경량화                |
|                       | - STT 모델 선택 및 경량화                |
|                       | - TTS 모델 선택 및 경량화                |
|                       | - 모델 파일 TensorFlow Lite 형식으로 변환|
+-----------------------+-----------------------------------------+
| 4. 앱 개발 및 통합   | - Android 앱 프로젝트 생성               |
|                       | - 모델 파일을 내부 저장소에 복사         |
|                       | - TensorFlow Lite 모델 로드 및 사용      |
|                       | - STT 및 TTS 기능 통합                   |
+-----------------------+-----------------------------------------+
| 5. 데이터베이스 설정 | - 사용자 데이터 저장을 위한 DB 설정      |
|                       | - 사용자 활동 로그 및 감정 상태 기록    |
|                       | - MongoDB 또는 SQLite 사용               |
+-----------------------+-----------------------------------------+
| 6. RAG 시스템 개발   | - 검색 모듈 구현 (Retrieval)            |
|                       | - 생성 모듈 구현 (Generation)           |
|                       | - RAG 통합 및 테스트                     |
+-----------------------+-----------------------------------------+
| 7. 인터페이스 개발   | - 사용자 인터페이스 디자인               |
|                       | - 음성 입력 및 출력 인터페이스 개발     |
|                       | - 사용자 맞춤형 대화 기능 구현          |
+-----------------------+-----------------------------------------+
| 8. 테스트 및 검증    | - 기능 테스트                            |
|                       | - 성능 테스트                            |
|                       | - 사용자 피드백 수집 및 개선             |
+-----------------------+-----------------------------------------+
| 9. 배포 및 유지보수  | - 앱 배포 (Google Play Store 등)         |
|                       | - 사용자 지원 및 버그 수정               |
|                       | - 지속적인 업데이트 및 기능 개선        |
+-----------------------+-----------------------------------------+
```
