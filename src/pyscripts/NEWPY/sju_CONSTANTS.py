STATE_MSG = {
    # dispatcher MSG
    100: '디스패처 로그 메세지',

    101: 'dispatcher를 준비합니다.',
    102: '기반 서비스를 초기화합니다. 이 작업은 2~3분이 소요됩니다.',
    103: '각 서비스의 브라우저 인증, 검색 폼 초기화를 수행합니다.',
    104: '초기화 진행 중 검색 서비스는 이용할 수 없습니다.',
    106: '단일 상세 검색 서비스 초기화가 완료되었습니다.',
    107: '다중 상세 검색 서비스 초기화가 완료되었습니다.',
    108: '다중 일반 검색 서비스 초기화가 완료되었습니다.',
    109: '저자명 기준 검색 서비스 초기화가 완료되었습니다.',

    201: '모든 서비스 초기화 완료.',
    301: '초기화 중 오류 발생.',
    302: 'wos 연결에 실패했습니다. 인터넷이나 접속 장소가 유효한 지 확인해주세요.',

    110: 'dispatcher가 준비되었습니다.',

    111: '단일 상세 검색을 호출합니다.',
    112: '단일 상세 검색을 마쳤습니다.',
    114: '단일 상세 검색을 마쳤습니다.',
    116: '단일 상세 검색을 마쳤습니다.',
    118: '단일 상세 검색을 마쳤습니다.',

    400: '알 수 없는 오류가 발생했습니다.',
    401: 'dispatcher와의 연결이 해제되었습니다. 프로그램을 재실행해주세요.',
    402: '알 수 없는 서비스 접근입니다.',

    500: 'dispatcher를 강제 종료합니다.',

    # single_search MSG
    1000: '상세 단일 검색 기능 로그 메세지',

    1001: '세션을 갱신합니다.',
    1101: '세션과 SID를 요청합니다.',
    1201: 'SID를 얻는데 성공하였습니다.',
    1301: ['SID를 얻는 중 오류가 발생했습니다.'],

    1002: '검색 프로세스를 시작합니다.',
    1102: '검색 결과를 요청합니다.',
    1202: '검색에 성공하였습니다.',
    1302: ['검색결과가 없습니다.', '검색 결과가 하나 이상입니다.', 'WOS 서버가 에러를 반환했습니다.'],

    1003: '상세 정보를 가져옵니다.',
    1103: '상세 정보 페이지를 요청합니다.',
    1203: '상세 정보를 가져오는데에 성공했습니다.',
    1303: ['상세 정보를 가져오는데에 실패했습니다.'],

    1004: '인용 논문 정보를 가져옵니다.',
    1104: '인용 리포트를 요청합니다.',
    1204: 'Fast 5000을 다운로드합니다.',
    1404: 'Fast 5000 데이터를 가공합니다.',
    1504: '기준 저자에 따라 검증합니다.',
    1304: ['논문을 인용한 논문이 없으므로 검색을 종료합니다.', '인용한 논문이 너무 많으므로 검색을 종료합니다.', '인용중 논문 검색 중 WOS 서버에서 에러를 보내왔습니다.'],

    1005: '',
    1105: '엑셀 파일 제작을 요청합니다.',
    1205: '파일 제작 요청에 성공했습니다.',
    1305: ['파일 제작 요청에 서버가 에러를 반환했습니다.'],

    1006: '',
    1106: '엑셀을 다운로드 받습니다.',
    1206: '엑셀 다운로드에 성공했습니다.',
    1306: ['서버가 엑셀이 아닌 에러를 반환했습니다.'],

    1200: ['상세 단일 검색을 완료했습니다.'],

    # multi_search MSG
    2000: '상세 엑셀 검색 기능 로그 메세지',

    2001: '',
    2101: '서브 스레드를 초기화합니다.',
    2201: '초기화가 완료되었습니다.',
    2301: ['서브 스레드 초기화를 실패했습니다.'],

    2002: '상세 엑셀 검색을 준비합니다',
    2102: '상세 엑셀 검색을 시작합니다.',
    2202: '상세 엑셀 검색을 완료했습니다.',
    2302: ['검색 중 에러가 발생했습니다.'],

    # author_search MSG
    3000: '저자 기준 검색 기능 로그 메세지',
    3000: '',
    3000: '',
    3000: '',
    3000: '',
    3000: '',
    3000: '',
}