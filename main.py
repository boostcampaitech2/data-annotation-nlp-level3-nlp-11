import argparse
from src.sentence_segmentation import SentenceSagmentation
from src.sentence_ner import SentenceNer
from src.crawling import Crawling
from src.EDA import Eda
from src.util.replace_entity import ReplaceEntity
from src.util.get_sentence_only import GetSentencenly

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # data dir
    parser.add_argument('--data_path', type=str, default="./data/original-data/")
    parser.add_argument('--output_dir',type=str, default="./output/")
    parser.add_argument('--raw_csv', type=str, default="raw_data.csv")
    parser.add_argument('--entity_csv', type=str, default="entity_data.csv")
    parser.add_argument('--split_result_data', type=int, default=0)
    parser.add_argument('--use_applywsd',type=bool, default=False)
    parser.add_argument('--use_crawling',type=bool, default=False)
    parser.add_argument('--show_entity_count',type=bool, default=False)
    args = parser.parse_args()


    # 크롤링시 data_path를 crwaling 데이터가 저장될 공간으로 변경해야함
    if args.use_crawling:
        text_array = [
            "운영 체제",
            "소스 코드",
            "통계학",
            "임베디드 시스템",
            "소프트웨어",
            "컴퓨터 그래픽스",
            "자료 구조",
            "전자공학",
            "리눅스",
            "영상 처리",
            "컴퓨터 프로그래밍",
            "확률론",
            "컴퓨터 하드웨어",
            "엘런 튜링",
            "튜링 테스트",
            "튜링 기계",
            "컴퓨터 네트워크",
            "알고리즘 분석",
            "컴퓨터 구조",
            "소프트웨어 버그",
            "빅 데이터",
            "안드로이드 (운영 체제)",
            "프로그래밍 언어",
            "컴퓨터 과학",
            "하드 디스크 드라이브",
            "중앙 처리 장치",
            "알고리즘",
            "암호학",
            "컴파일러",
            "사운드 카드",
            "증강 현실",
            "메인보드",
        ]
        Crawling(args,text_array)

    # {output_dir}{raw_csv} 생성
    SentenceSagmentation(args)

    # # {output_dir}{raw_csv} 기반 {output_dir}{entity_csv} 생성
    SentenceNer(args)

    # replace (entity 변경 ./src/util/replace_entity.py 에서 regex 수정)
    ReplaceEntity(args)

    if args.show_entity_count:
        Eda(args)

    # 전체문장을 N개로 분리 진행
    if args.split_result_data !=0:
        GetSentencenly(args).split_sentence(args.split_result_data)