# 2020 GJAI 해커톤 2020.09.24

## 💡 해커톤 주제
* 코로나19로 인한 언택트시대에 알맞은 서비스 개발
  * 인공지능
  * 웹서비스
  * 언택트

## 💡 아이디어
* "꼭 만나서만 봉사활동을 해야하나요?" 몸은 언택트! 마음은 컨택트! 언택트시대에 맞춤화된 비대면 봉사활동 웹서비스 개발.
* 코로나19의 장기화로 인하여 봉사활동이 필요하지만 코로나로 인하여 불안한 사람들! 하지만 기존 봉사활동을 찾을수 있는 서비스에서는 대부분이 대면을 요구하는 봉사활동이며, 일부 비대면을 통한 봉사활동이 올라와 있으나 사용자가 일일이 검색을 하여 찾아야 하는 번거로움이 있음.

## 💡 서비스계획
* 처음에는 우리들이 직접 각 봉사사이트를 통하여 크롤링하여 비대면봉사활동을 수집하여 각 봉사활동에 해당하는 정보와 함께 출처링크를 제공. 이후 사용자가 늘어남에 따라 봉사활동을 제공하는 관계자분들이 직접 사이트로 들어와서 글을 올리는 등 초기단계와 같이 직접적인 봉사활동 데이터수집의 비중은 줄이고 관리위주로 운영하고 봉사관계자와 봉사자들로인한 자체내부적으로 돌아가게끔 운영.

## 💡 구현계획
* Django를 이용하여 웹사이트 제작
  * 사용자 회원가입(봉사관계자, 봉사자 구별하여)
  * 사용자가 원하는 검색을 위한 리스트
    * ![봉사활동검색리스트1](./img, icon/봉사활동검색리스트.png)
    * ![봉사활동검색리스트2](./img, icon/봉사활동검색리스트2.png)
  * 전체 봉사리스트가 올라와있는 목록현황테이블
    * ![봉사활동모집리스트](./img, icon/봉사활동모집리스트.png)
  * 봉사관계자가 글을 적을수있도록 하는 페이지와 해당정보들이 적혀있는 페이지
    * ![봉사활동상세정보](./img, icon/봉사활동상세정보.png)
* 사용자 회원가입과 봉사활동데이터들이 들어간 DB 구축
