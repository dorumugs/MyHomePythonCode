GDP_MAPPING = {
    'info': {'index_nm': 'gdp'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "년": {
                    "type": "integer"
                },
                "분기": {
                    "type": "integer"
                },
                "Nominal_GDP_분기": {
                    "type": "float"
                },
                "Real_GDP_분기": {
                    "type": "float"
                },
                "Nominal_GDP_년": {
                    "type": "float"
                },
                "Real_GDP_년": {
                    "type": "float"
                },
                "날짜": {
                    "type": "date"
                },
            }
        }
    },
}

POPULATION_MAPPING = {
    'info': {'index_nm': 'population'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "행정구역별_읍면동": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "총인구_명": {
                    "type": "integer"
                },
                "남자_명": {
                    "type": "integer"
                },
                "여자_명": {
                    "type": "integer"
                },
                "내국인-계_명": {
                    "type": "integer"
                },
                "내국인-남자_명": {
                    "type": "integer"
                },
                "내국인-여자_명": {
                    "type": "integer"
                },
                "외국인-계_명": {
                    "type": "integer"
                },
                "외국인-남자_명": {
                    "type": "integer"
                },
                "외국인-여자_명": {
                    "type": "integer"
                },
                "가구-계_가구": {
                    "type": "integer"
                },
                "일반가구_가구": {
                    "type": "integer"
                },
                "집단가구_가구": {
                    "type": "integer"
                },
                "외국인가구_가구": {
                    "type": "integer"
                },
                "주택-계_호": {
                    "type": "integer"
                },
                "단독주택_호": {
                    "type": "integer"
                },
                "아파트_호": {
                    "type": "integer"
                },
                "연립주택_호": {
                    "type": "integer"
                },
                "다세대주택_호": {
                    "type": "integer"
                },
                "비거주용건물내주택_호": {
                    "type": "integer"
                },
                "주택이외의거처_호": {
                    "type": "integer"
                },
                "시도명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
            }
        }
    },
}

PRICE_MAPPING = {
    'info': {'index_nm': 'price'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "년": {
                    "type": "integer"
                },
                "분기": {
                    "type": "integer"
                },
                "총지수_물가_분기": {
                    "type": "float"
                },
                "총지수_물가_년": {
                    "type": "float"
                },
                "날짜": {
                    "type": "date"
                },
            }
        }
    },
}

UNSOLD_MAPPING = {
    'info': {'index_nm': 'unsold'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "시도명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "년": {
                    "type": "integer"
                },
                "분기": {
                    "type": "integer"
                },
                "미분양_개수_분기": {
                    "type": "integer"
                },
                "미분양_개수_년": {
                    "type": "integer"
                },
                "날짜": {
                    "type": "date"
                },
            }
        }
    },
}

REAL_ESTATE_MAPPING_AC_PRE = {
    'info': {'index_nm': 'real_estate_actual_tx_pre'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "시도명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "시군구명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "법정동": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "지번": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "지역코드": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "건축년도": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "아파트": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "전용면적": {
                    "type": "float"
                },
                "층": {
                    "type": "integer"
                },
                "거래일": {
                    "type": "date"
                },
                "거래금액": {
                    "type": "float"
                },
                "년": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "월": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "일": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "분기": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
            }
        }
    },
}

REAL_ESTATE_MAPPING_AC = {
    'info': {'index_nm': 'real_estate_actual_tx'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "시도명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "시군구명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "법정동": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "지번": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "지역코드": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "건축년도": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "아파트": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "전용면적": {
                    "type": "float"
                },
                "층": {
                    "type": "integer"
                },
                "거래일": {
                    "type": "date"
                },
                "거래금액": {
                    "type": "float"
                },
                "년": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "월": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "일": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "분기": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "총인구_명": {
                    "type": "integer"
                },
                "Nominal_GDP_년": {
                    "type": "float"
                },
                "Nominal_GDP_분기": {
                    "type": "float"
                },
                "Real_GDP_년": {
                    "type": "float"
                },
                "Real_GDP_분기": {
                    "type": "float"
                },
                "총지수_물가_년": {
                    "type": "float"
                },
                "총지수_물가_분기": {
                    "type": "float"
                },
                "미분양_개수_년": {
                    "type": "integer"
                },
                "미분양_개수_분기": {
                    "type": "integer"
                },
                "거래금액_년": {
                    "type": "float"
                },
                "거래금액_분기": {
                    "type": "float"
                },
                "거래금액_월": {
                    "type": "float"
                },
                "보증금액_년": {
                    "type": "float"
                },
                "보증금액_분기": {
                    "type": "float"
                },
                "보증금액_월": {
                    "type": "float"
                },
                "전세가율_년": {
                    "type": "float"
                },
                "전세가율_분기": {
                    "type": "float"
                },
                "전세가율_월": {
                    "type": "float"
                }
            }
        }
    },
}

REAL_ESTATE_MAPPING_CH_PRE = {
    'info': {'index_nm': 'real_estate_chartered_rent_tx_pre'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "시도명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "시군구명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "법정동": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "지번": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "지역코드": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "건축년도": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "아파트": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "전용면적": {
                    "type": "float"
                },
                "층": {
                    "type": "integer"
                },
                "거래일": {
                    "type": "date"
                },
                "거래금액": {
                    "type": "float"
                },
                "보증금액": {
                    "type": "float"
                },
                "월세금액": {
                    "type": "float"
                },
                "년": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "월": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "일": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "분기": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
            }
        }
    },
}

REAL_ESTATE_MAPPING_CH = {
    'info': {'index_nm': 'real_estate_chartered_rent_tx'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "시도명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "시군구명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "법정동": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "지번": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "지역코드": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "건축년도": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "아파트": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "전용면적": {
                    "type": "float"
                },
                "층": {
                    "type": "integer"
                },
                "거래일": {
                    "type": "date"
                },
                "거래금액": {
                    "type": "float"
                },
                "보증금액": {
                    "type": "float"
                },
                "월세금액": {
                    "type": "float"
                },
                "년": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "월": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "일": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "분기": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "총인구_명": {
                    "type": "integer"
                },
                "Nominal_GDP": {
                    "type": "float"
                },
                "Real_GDP": {
                    "type": "float"
                },
                "총지수_물가_년": {
                    "type": "float"
                },
                "총지수_물가_분기": {
                    "type": "float"
                },
                "미분양_개수_년": {
                    "type": "integer"
                },
                "미분양_개수_분기": {
                    "type": "integer"
                },
                "거래금액_년": {
                    "type": "float"
                },
                "거래금액_분기": {
                    "type": "float"
                },
                "거래금액_월": {
                    "type": "float"
                },
                "보증금액_년": {
                    "type": "float"
                },
                "보증금액_분기": {
                    "type": "float"
                },
                "보증금액_월": {
                    "type": "float"
                },
                "전세가율_년": {
                    "type": "float"
                },
                "전세가율_분기": {
                    "type": "float"
                },
                "전세가율_월": {
                    "type": "float"
                }
            }
        }
    },
}

AC_CH_MAPPING = {
    'info': {'index_nm': 'ac_ch'},
    'mapping': {
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "시도명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "시군구명": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "년": {
                    "type": "integer"
                },
                "월": {
                    "type": "integer"
                },
                "분기": {
                    "type": "integer"
                },
                "거래금액_년": {
                    "type": "float"
                },
                "거래금액_분기": {
                    "type": "float"
                },
                "거래금액_월": {
                    "type": "float"
                },
                "보증금액_년": {
                    "type": "float"
                },
                "보증금액_분기": {
                    "type": "float"
                },
                "보증금액_월": {
                    "type": "float"
                },
                "전세가율_년": {
                    "type": "float"
                },
                "전세가율_분기": {
                    "type": "float"
                },
                "전세가율_월": {
                    "type": "float"
                },
                "총인구_명": {
                    "type": "integer"
                },
                "Nominal_GDP_년": {
                    "type": "integer"
                },
                "Nominal_GDP_분기": {
                    "type": "integer"
                },
                "Real_GDP_년": {
                    "type": "float"
                },
                "Real_GDP_분기": {
                    "type": "float"
                },
                "총지수_물가_년": {
                    "type": "float"
                },
                "총지수_물가_분기": {
                    "type": "float"
                },
                "미분양_개수_년": {
                    "type": "integer"
                },
                "미분양_개수_분기": {
                    "type": "integer"
                },
                "거래금액_월_증감률": {
                    "type": "float"
                },
                "거래금액_년_증감률": {
                    "type": "float"
                },
                "거래금액_분기_증감률": {
                    "type": "float"
                },
                "보증금액_월_증감률": {
                    "type": "float"
                },
                "보증금액_년_증감률": {
                    "type": "float"
                },
                "보증금액_분기_증감률": {
                    "type": "float"
                },
                "전세가율_월_증감률": {
                    "type": "float"
                },
                "전세가율_년_증감률": {
                    "type": "float"
                },
                "전세가율_분기_증감률": {
                    "type": "float"
                },
                "총지수_물가_분기_증감률": {
                    "type": "float"
                },
                "총지수_물가_년_증감률": {
                    "type": "float"
                },
                "미분양_개수_분기_증감률": {
                    "type": "float"
                },
                "미분양_개수_년_증감률": {
                    "type": "float"
                },
                "Nominal_GDP_분기_증감률": {
                    "type": "float"
                },
                "Nominal_GDP_년_증감률": {
                    "type": "float"
                },
                "Real_GDP_분기_증감률": {
                    "type": "float"
                },
                "Real_GDP_년_증감률": {
                    "type": "float"
                },
                "날짜": {
                    "type": "date",
                    "format": "yyyy-MM-dd"
                },
            }
        }
    },
}