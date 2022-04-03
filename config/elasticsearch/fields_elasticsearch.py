from datetime import datetime


def gdp_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "년": dataframe.at[idx, "년"],
        "분기": dataframe.at[idx, "분기"],
        "Nominal_GDP_분기": dataframe.at[idx, "Nominal_GDP_분기"],
        "Real_GDP_분기": dataframe.at[idx, "Real_GDP_분기"],
        "Nominal_GDP_년": dataframe.at[idx, "Nominal_GDP_년"],
        "Real_GDP_년": dataframe.at[idx, "Real_GDP_년"],
        "날짜": dataframe.at[idx, "날짜"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }


def population_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "행정구역별_읍면동": dataframe.at[idx, "행정구역별_읍면동"],
        "총인구_명": dataframe.at[idx, "총인구_명"],
        "남자_명": dataframe.at[idx, "남자_명"],
        "여자_명": dataframe.at[idx, "여자_명"],
        "내국인-계_명": dataframe.at[idx, "내국인-계_명"],
        "내국인-남자_명": dataframe.at[idx, "내국인-남자_명"],
        "내국인-여자_명": dataframe.at[idx, "내국인-여자_명"],
        "외국인-계_명": dataframe.at[idx, "외국인-계_명"],
        "외국인-남자_명": dataframe.at[idx, "외국인-남자_명"],
        "외국인-여자_명": dataframe.at[idx, "외국인-여자_명"],
        "가구-계_가구": dataframe.at[idx, "가구-계_가구"],
        "일반가구_가구": dataframe.at[idx, "일반가구_가구"],
        "집단가구_가구": dataframe.at[idx, "집단가구_가구"],
        "외국인가구_가구": dataframe.at[idx, "외국인가구_가구"],
        "주택-계_호": dataframe.at[idx, "주택-계_호"],
        "단독주택_호": dataframe.at[idx, "단독주택_호"],
        "아파트_호": dataframe.at[idx, "아파트_호"],
        "연립주택_호": dataframe.at[idx, "연립주택_호"],
        "다세대주택_호": dataframe.at[idx, "다세대주택_호"],
        "비거주용건물내주택_호": dataframe.at[idx, "비거주용건물내주택_호"],
        "주택이외의거처_호": dataframe.at[idx, "주택이외의거처_호"],
        "시도명": dataframe.at[idx, "시도명"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }


def price_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "년": dataframe.at[idx, "년"],
        "분기": dataframe.at[idx, "분기"],
        "총지수_물가_분기": dataframe.at[idx, "총지수_물가_분기"],
        "총지수_물가_년": dataframe.at[idx, "총지수_물가_년"],
        "날짜": dataframe.at[idx, "날짜"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }


def unsold_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "시도명": dataframe.at[idx, "시도명"],
        "년": dataframe.at[idx, "년"],
        "분기": dataframe.at[idx, "분기"],
        "미분양_개수_분기": dataframe.at[idx, "미분양_개수_분기"],
        "미분양_개수_년": dataframe.at[idx, "미분양_개수_년"],
        "날짜": dataframe.at[idx, "날짜"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }


def real_estate_ac_pre_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "시도명": dataframe.at[idx, "시도명"],
        "시군구명": dataframe.at[idx, "시군구명"],
        "법정동": dataframe.at[idx, "법정동"],
        "지번": dataframe.at[idx, "지번"],
        "지역코드": dataframe.at[idx, "지역코드"],
        "건축년도": dataframe.at[idx, "건축년도"],
        "아파트": dataframe.at[idx, "아파트"],
        "전용면적": dataframe.at[idx, "전용면적"],
        "층": dataframe.at[idx, "층"],
        "거래일": dataframe.at[idx, "거래일"],
        "거래금액": dataframe.at[idx, "거래금액"],
        "년": dataframe.at[idx, "년"],
        "월": dataframe.at[idx, "월"],
        "일": dataframe.at[idx, "일"],
        "분기": dataframe.at[idx, "분기"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }


def real_estate_ac_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "시도명": dataframe.at[idx, "시도명"],
        "시군구명": dataframe.at[idx, "시군구명"],
        "법정동": dataframe.at[idx, "법정동"],
        "지번": dataframe.at[idx, "지번"],
        "지역코드": dataframe.at[idx, "지역코드"],
        "건축년도": dataframe.at[idx, "건축년도"],
        "아파트": dataframe.at[idx, "아파트"],
        "전용면적": dataframe.at[idx, "전용면적"],
        "층": dataframe.at[idx, "층"],
        "거래일": dataframe.at[idx, "거래일"],
        "거래금액": dataframe.at[idx, "거래금액"],
        "년": dataframe.at[idx, "년"],
        "월": dataframe.at[idx, "월"],
        "일": dataframe.at[idx, "일"],
        "분기": dataframe.at[idx, "분기"],
        "총인구_명": dataframe.at[idx, "총인구_명"],
        "Nominal_GDP_년": dataframe.at[idx, "Nominal_GDP_년"],
        "Nominal_GDP_분기": dataframe.at[idx, "Nominal_GDP_분기"],
        "Real_GDP_년": dataframe.at[idx, "Real_GDP_년"],
        "Real_GDP_분기": dataframe.at[idx, "Real_GDP_분기"],
        "총지수_물가_년": dataframe.at[idx, "총지수_물가_년"],
        "총지수_물가_분기": dataframe.at[idx, "총지수_물가_분기"],
        "미분양_개수_년": dataframe.at[idx, "미분양_개수_년"],
        "미분양_개수_분기": dataframe.at[idx, "미분양_개수_분기"],
        "거래금액_년": dataframe.at[idx, "거래금액_년"],
        "거래금액_분기": dataframe.at[idx, "거래금액_분기"],
        "거래금액_월": dataframe.at[idx, "거래금액_월"],
        "보증금액_년": dataframe.at[idx, "보증금액_년"],
        "보증금액_분기": dataframe.at[idx, "보증금액_분기"],
        "보증금액_월": dataframe.at[idx, "보증금액_월"],
        "전세가율_년": dataframe.at[idx, "전세가율_년"],
        "전세가율_분기": dataframe.at[idx, "전세가율_분기"],
        "전세가율_월": dataframe.at[idx, "전세가율_월"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }


def real_estate_ch_pre_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "시도명": dataframe.at[idx, "시도명"],
        "시군구명": dataframe.at[idx, "시군구명"],
        "법정동": dataframe.at[idx, "법정동"],
        "지번": dataframe.at[idx, "지번"],
        "지역코드": dataframe.at[idx, "지역코드"],
        "건축년도": dataframe.at[idx, "건축년도"],
        "아파트": dataframe.at[idx, "아파트"],
        "전용면적": dataframe.at[idx, "전용면적"],
        "층": dataframe.at[idx, "층"],
        "거래일": dataframe.at[idx, "거래일"],
        "보증금액": dataframe.at[idx, "보증금액"],
        "월세금액": dataframe.at[idx, "월세금액"],
        "년": dataframe.at[idx, "년"],
        "월": dataframe.at[idx, "월"],
        "일": dataframe.at[idx, "일"],
        "분기": dataframe.at[idx, "분기"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }


def real_estate_ch_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "시도명": dataframe.at[idx, "시도명"],
        "시군구명": dataframe.at[idx, "시군구명"],
        "법정동": dataframe.at[idx, "법정동"],
        "지번": dataframe.at[idx, "지번"],
        "지역코드": dataframe.at[idx, "지역코드"],
        "건축년도": dataframe.at[idx, "건축년도"],
        "아파트": dataframe.at[idx, "아파트"],
        "전용면적": dataframe.at[idx, "전용면적"],
        "층": dataframe.at[idx, "층"],
        "거래일": dataframe.at[idx, "거래일"],
        "보증금액": dataframe.at[idx, "보증금액"],
        "월세금액": dataframe.at[idx, "월세금액"],
        "년": dataframe.at[idx, "년"],
        "월": dataframe.at[idx, "월"],
        "일": dataframe.at[idx, "일"],
        "분기": dataframe.at[idx, "분기"],
        "총인구_명": dataframe.at[idx, "총인구_명"],
        "Nominal_GDP_년": dataframe.at[idx, "Nominal_GDP_년"],
        "Nominal_GDP_분기": dataframe.at[idx, "Nominal_GDP_분기"],
        "Real_GDP_년": dataframe.at[idx, "Real_GDP_년"],
        "Real_GDP_분기": dataframe.at[idx, "Real_GDP_분기"],
        "총지수_물가_년": dataframe.at[idx, "총지수_물가_년"],
        "총지수_물가_분기": dataframe.at[idx, "총지수_물가_분기"],
        "미분양_개수_년": dataframe.at[idx, "미분양_개수_년"],
        "미분양_개수_분기": dataframe.at[idx, "미분양_개수_분기"],
        "거래금액_년": dataframe.at[idx, "거래금액_년"],
        "거래금액_분기": dataframe.at[idx, "거래금액_분기"],
        "거래금액_월": dataframe.at[idx, "거래금액_월"],
        "보증금액_년": dataframe.at[idx, "보증금액_년"],
        "보증금액_분기": dataframe.at[idx, "보증금액_분기"],
        "보증금액_월": dataframe.at[idx, "보증금액_월"],
        "전세가율_년": dataframe.at[idx, "전세가율_년"],
        "전세가율_분기": dataframe.at[idx, "전세가율_분기"],
        "전세가율_월": dataframe.at[idx, "전세가율_월"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }


def ac_ch_fields(index_nm, dataframe, idx):
    return {
        "_index": index_nm,
        "시도명": dataframe.at[idx, "시도명"],
        "시군구명": dataframe.at[idx, "시군구명"],
        "년": dataframe.at[idx, "년"],
        "월": dataframe.at[idx, "월"],
        "분기": dataframe.at[idx, "분기"],
        "거래금액_년": dataframe.at[idx, "거래금액_년"],
        "거래금액_분기": dataframe.at[idx, "거래금액_분기"],
        "거래금액_월": dataframe.at[idx, "거래금액_월"],
        "보증금액_년": dataframe.at[idx, "보증금액_년"],
        "보증금액_분기": dataframe.at[idx, "보증금액_분기"],
        "보증금액_월": dataframe.at[idx, "보증금액_월"],
        "전세가율_년": dataframe.at[idx, "전세가율_년"],
        "전세가율_분기": dataframe.at[idx, "전세가율_분기"],
        "전세가율_월": dataframe.at[idx, "전세가율_월"],
        "총인구_명": dataframe.at[idx, "총인구_명"],
        "Nominal_GDP_년": dataframe.at[idx, "Nominal_GDP_년"],
        "Nominal_GDP_분기": dataframe.at[idx, "Nominal_GDP_분기"],
        "Real_GDP_년": dataframe.at[idx, "Real_GDP_년"],
        "Real_GDP_분기": dataframe.at[idx, "Real_GDP_분기"],
        "총지수_물가_년": dataframe.at[idx, "총지수_물가_년"],
        "총지수_물가_분기": dataframe.at[idx, "총지수_물가_분기"],
        "미분양_개수_년": dataframe.at[idx, "미분양_개수_년"],
        "미분양_개수_분기": dataframe.at[idx, "미분양_개수_분기"],
        "거래금액_월_증감률": dataframe.at[idx, "거래금액_월_증감률"],
        "거래금액_년_증감률": dataframe.at[idx, "거래금액_년_증감률"],
        "거래금액_분기_증감률": dataframe.at[idx, "거래금액_분기_증감률"],
        "보증금액_월_증감률": dataframe.at[idx, "보증금액_월_증감률"],
        "보증금액_년_증감률": dataframe.at[idx, "보증금액_년_증감률"],
        "보증금액_분기_증감률": dataframe.at[idx, "보증금액_분기_증감률"],
        "전세가율_월_증감률": dataframe.at[idx, "전세가율_월_증감률"],
        "전세가율_년_증감률": dataframe.at[idx, "전세가율_년_증감률"],
        "전세가율_분기_증감률": dataframe.at[idx, "전세가율_분기_증감률"],
        "총지수_물가_분기_증감률": dataframe.at[idx, "총지수_물가_분기_증감률"],
        "총지수_물가_년_증감률": dataframe.at[idx, "총지수_물가_년_증감률"],
        "미분양_개수_분기_증감률": dataframe.at[idx, "미분양_개수_분기_증감률"],
        "미분양_개수_년_증감률": dataframe.at[idx, "미분양_개수_년_증감률"],
        "Nominal_GDP_분기_증감률": dataframe.at[idx, "Nominal_GDP_분기_증감률"],
        "Nominal_GDP_년_증감률": dataframe.at[idx, "Nominal_GDP_년_증감률"],
        "Real_GDP_분기_증감률": dataframe.at[idx, "Real_GDP_분기_증감률"],
        "Real_GDP_년_증감률": dataframe.at[idx, "Real_GDP_년_증감률"],
        "날짜": dataframe.at[idx, "날짜"],
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }
