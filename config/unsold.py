# 미분양 정보 세팅

UNSOLD_URL = 'https://kosis.kr/statHtml/makeLarge.do'
UNSOLD_COOKIES = {
    'newKOSIS2020StatisCtgrSettingCookie_1': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CI1%7CH2%7CN1%7CN2%7CT%7CU%7CK1%7CK2%7CJ1%7CJ2%7CL%7CM1%7CM2%7CO%7CO2%7CP%7CQ%7CR%7CS1%7CS2%7CI2%7CV',
    'mb': 'N',
    'JSESSIONID': 'EnL7qKu1dUa9sWANoarCunMr1Ko8iHEmxcZlMeTPO3wtw2T6JwUgaD7aVBnSh6KM.STAT_WAS1_servlet_engine5',
}
UNSOLD_HEADERS = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://kosis.kr',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://kosis.kr/statHtml/statHtml.do?orgId=116&tblId=DT_MLTM_2080&vw_cd=&list_id=&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=E1&docId=0317427997&markType=S&itmNm=%EC%A0%84%EA%B5%AD',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
}
UNSOLD_DATA = [
    ('orgId', '116'),
    ('tblId', 'DT_MLTM_2080'),
    ('language', 'ko'),
    ('file', ''),
    ('analText', ''),
    ('scrId', ''),
    ('fieldList',
     '[{"targetId":"PRD","targetValue":"","prdValue":"M,202102,202101,202012,202011,202010,202009,202008,202007,202006,202005,202004,202003,202002,202001,201912,201911,201910,201909,201908,201907,201906,201905,201904,201903,201902,201901,201812,201811,201810,201809,201808,201807,201806,201805,201804,201803,201802,201801,201712,201711,201710,201709,201708,201707,201706,201705,201704,201703,201702,201701,201612,201611,201610,201609,201608,201607,201606,201605,201604,201603,201602,201601,201512,201511,201510,201509,201508,201507,201506,201505,201504,201503,201502,201501,201412,201411,201410,201409,201408,201407,201406,201405,201404,201403,201402,201401,201312,201311,201310,201309,201308,201307,201306,201305,201304,201303,201302,201301,201212,201211,201210,201209,201208,201207,201206,201205,201204,201203,201202,201201,201112,201111,201110,201109,201108,201107,201106,201105,201104,201103,201102,201101,201012,201011,201010,201009,201008,201007,201006,201005,201004,201003,201002,201001,200912,200911,200910,200909,200908,200907,200906,200905,200904,200903,200902,200901,200812,200811,200810,200809,200808,200807,200806,200805,200804,200803,200802,200801,200712,200711,200710,200709,200708,200707,200706,200705,200704,200703,200702,200701,@"},{"targetId":"ITM_ID","targetValue":"13103792722T1","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0001","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0002","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0006","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0007","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0008","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0009","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0011","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0012","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0013","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0014","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0015","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0016","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0017","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0018","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0019","prdValue":""},{"targetId":"OV_L2_ID","targetValue":"13102792722B.0001","prdValue":""},{"targetId":"OV_L2_ID","targetValue":"13102792722B.0002","prdValue":""},{"targetId":"OV_L2_ID","targetValue":"13102792722B.0003","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0001","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0002","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0003","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0004","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0005","prdValue":""}]'),
    ('colAxis', 'TIME,13101792722B,13101792722C'),
    ('rowAxis', '13101792722A'),
    ('isFirst', 'N'),
    ('contextPath', '/statHtml'),
    ('ordColIdx', ''),
    ('ordType', ''),
    ('logSeq', '106033059'),
    ('vwCd', ''),
    ('listId', ''),
    ('connPath', 'E1'),
    ('statId', '1998033'),
    ('pub', ''),
    ('pubLog', '4'),
    ('viewKind', '2'),
    ('viewSubKind', '2_7_2'),
    ('doAnal', 'N'),
    ('analType', ''),
    ('analCmpr', ''),
    ('analTime', ''),
    ('analCombo', ''),
    ('originData', ''),
    ('analClass', ''),
    ('analItem', ''),
    ('obj_var_id', ''),
    ('itm_id', ''),
    ('mode', ''),
    ('dataOpt', 'ko'),
    ('noSelect', ''),
    ('view', 'csv'),
    ('existStblCmmtKor', 'Y'),
    ('existStblCmmtEng', 'N'),
    ('classAllArr',
     '[{"objVarId":"13101792722A","ovlSn":"1"},{"objVarId":"13101792722B","ovlSn":"2"},{"objVarId":"13101792722C","ovlSn":"3"}]'),
    ('classSet',
     '[{"objVarId":"13101792722A","ovlSn":"1","visible":"true"},{"objVarId":"13101792722B","ovlSn":"2","visible":"true"},{"objVarId":"13101792722C","ovlSn":"3","visible":"true"}]'),
    ('selectAllFlag', 'N'),
    ('selectTimeRangeCnt', '3'),
    ('periodStr', 'M'),
    ('funcPrdSe', ''),
    ('tblNm', '\uADDC\uBAA8\uBCC4 \uBBF8\uBD84\uC591\uD604\uD669'),
    ('tblEngNm', 'Unsold Housings by Size'),
    ('isChangedDataOpt', ''),
    ('itemMultiply', '285'),
    ('dimCo', '152'),
    ('dbUser', 'NSI.'),
    ('usePivot', 'N'),
    ('isChangedTableType', 'N'),
    ('isChangedPeriodCo', 'N'),
    ('isChangedPrdSort', 'N'),
    ('p_chkStatus', ''),
    ('p_objVarId', ''),
    ('p_lvl', ''),
    ('p_logicFlag', 'Y'),
    ('p_classAllChkYn', 'Y'),
    ('p_classAllSelectYn', 'N'),
    ('useAddFuncLog', ''),
    ('chargerLvl', ''),
    ('st', ''),
    ('new_win', ''),
    ('first_open', 'Y'),
    ('debug', ''),
    ('maxCellOver', ''),
    ('reqCellCnt', '855'),
    ('inheritYn', 'N'),
    ('originOrgId', ''),
    ('originTblId', ''),
    ('pubSeType', ''),
    ('relChkOrgId', ''),
    ('relChkTblId', ''),
    ('highLightStr',
     '[{"targetId":"PRD","targetValue":"202102","prdSe":"M"},{"targetId":"ITM","targetValue":"13103792722T1"},{"targetId":"VAL","val":"15,786","originVal":"15786"},{"targetId":"CLASS","value":{"objId1":"13101792722A","OV_L1_ID":"13102792722A.0001","objId2":"13101792722B","OV_L2_ID":"13102792722B.0001","objId3":"13101792722C","OV_L3_ID":"13102792722C.0001"},"classCnt":3}]'),
    ('markType', 'S'),
    ('docId', '3174'),
    ('itmNm', '\uC804\uAD6D'),
    ('tableType', 'default'),
    ('dataOpt2', 'ko'),
    ('periodCo', ''),
    ('enableLevelExpr', 'Y'),
    ('prdSort', 'desc'),
    ('findData', 'on'),
    ('compValue', ''),
    ('compValue01', ''),
    ('compValue02', ''),
    ('expDash', 'Y'),
    ('downGridFileType', 'xlsx'),
    ('downGridCellMerge', 'Y'),
    ('downGridMeta', 'Y'),
    ('downSort', 'asc'),
    ('pointType', 'screen'),
    ('downLargeFileType', 'csv'),
    ('downLargeExprType', '1'),
    ('downLargeSort', 'asc'),
    ('naviInfo', 'tabItemText'),
    ('naviInfo', '13101792722A'),
    ('naviInfo', '13101792722B'),
    ('naviInfo', '13101792722C'),
    ('naviInfo', 'tabTimeText'),
    ('itemChkLi', '13103792722T1'),
    ('classAllSelect', 'on'),
    ('classAllSelect', 'on'),
    ('classAllSelect', 'on'),
    ('classLvlAllChk1_1', 'on'),
    ('classChkLi1_1', '13102792722A.0001='),
    ('classChkLi1_1', '13102792722A.0002='),
    ('classChkLi1_1', '13102792722A.0003='),
    ('classChkLi1_1', '13102792722A.0004='),
    ('classChkLi1_1', '13102792722A.0005='),
    ('classChkLi1_1', '13102792722A.0006='),
    ('classChkLi1_1', '13102792722A.0007='),
    ('classChkLi1_1', '13102792722A.0008='),
    ('classChkLi1_1', '13102792722A.0009='),
    ('classChkLi1_1', '13102792722A.0010='),
    ('classChkLi1_1', '13102792722A.0011='),
    ('classChkLi1_1', '13102792722A.0012='),
    ('classChkLi1_1', '13102792722A.0013='),
    ('classChkLi1_1', '13102792722A.0014='),
    ('classChkLi1_1', '13102792722A.0015='),
    ('classChkLi1_1', '13102792722A.0016='),
    ('classChkLi1_1', '13102792722A.0017='),
    ('classChkLi1_1', '13102792722A.0018='),
    ('classChkLi1_1', '13102792722A.0019='),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('classLvlAllChk2_1', 'on'),
    ('classChkLi2_1', '13102792722B.0001='),
    ('classChkLi2_1', '13102792722B.0002='),
    ('classChkLi2_1', '13102792722B.0003='),
    ('classLvlAllChk3_1', 'on'),
    ('classChkLi3_1', '13102792722C.0001='),
    ('classChkLi3_1', '13102792722C.0002='),
    ('classChkLi3_1', '13102792722C.0003='),
    ('classChkLi3_1', '13102792722C.0004='),
    ('classChkLi3_1', '13102792722C.0005='),
    ('headCheck', 'M'),
    ('timeChkM', '202102'),
    ('timeChkM', '202101'),
    ('timeChkM', '202012'),
    ('timeChkM', '202011'),
    ('timeChkM', '202010'),
    ('timeChkM', '202009'),
    ('timeChkM', '202008'),
    ('timeChkM', '202007'),
    ('timeChkM', '202006'),
    ('timeChkM', '202005'),
    ('timeChkM', '202004'),
    ('timeChkM', '202003'),
    ('timeChkM', '202002'),
    ('timeChkM', '202001'),
    ('timeChkM', '201912'),
    ('timeChkM', '201911'),
    ('timeChkM', '201910'),
    ('timeChkM', '201909'),
    ('timeChkM', '201908'),
    ('timeChkM', '201907'),
    ('timeChkM', '201906'),
    ('timeChkM', '201905'),
    ('timeChkM', '201904'),
    ('timeChkM', '201903'),
    ('timeChkM', '201902'),
    ('timeChkM', '201901'),
    ('timeChkM', '201812'),
    ('timeChkM', '201811'),
    ('timeChkM', '201810'),
    ('timeChkM', '201809'),
    ('timeChkM', '201808'),
    ('timeChkM', '201807'),
    ('timeChkM', '201806'),
    ('timeChkM', '201805'),
    ('timeChkM', '201804'),
    ('timeChkM', '201803'),
    ('timeChkM', '201802'),
    ('timeChkM', '201801'),
    ('timeChkM', '201712'),
    ('timeChkM', '201711'),
    ('timeChkM', '201710'),
    ('timeChkM', '201709'),
    ('timeChkM', '201708'),
    ('timeChkM', '201707'),
    ('timeChkM', '201706'),
    ('timeChkM', '201705'),
    ('timeChkM', '201704'),
    ('timeChkM', '201703'),
    ('timeChkM', '201702'),
    ('timeChkM', '201701'),
    ('timeChkM', '201612'),
    ('timeChkM', '201611'),
    ('timeChkM', '201610'),
    ('timeChkM', '201609'),
    ('timeChkM', '201608'),
    ('timeChkM', '201607'),
    ('timeChkM', '201606'),
    ('timeChkM', '201605'),
    ('timeChkM', '201604'),
    ('timeChkM', '201603'),
    ('timeChkM', '201602'),
    ('timeChkM', '201601'),
    ('timeChkM', '201512'),
    ('timeChkM', '201511'),
    ('timeChkM', '201510'),
    ('timeChkM', '201509'),
    ('timeChkM', '201508'),
    ('timeChkM', '201507'),
    ('timeChkM', '201506'),
    ('timeChkM', '201505'),
    ('timeChkM', '201504'),
    ('timeChkM', '201503'),
    ('timeChkM', '201502'),
    ('timeChkM', '201501'),
    ('timeChkM', '201412'),
    ('timeChkM', '201411'),
    ('timeChkM', '201410'),
    ('timeChkM', '201409'),
    ('timeChkM', '201408'),
    ('timeChkM', '201407'),
    ('timeChkM', '201406'),
    ('timeChkM', '201405'),
    ('timeChkM', '201404'),
    ('timeChkM', '201403'),
    ('timeChkM', '201402'),
    ('timeChkM', '201401'),
    ('timeChkM', '201312'),
    ('timeChkM', '201311'),
    ('timeChkM', '201310'),
    ('timeChkM', '201309'),
    ('timeChkM', '201308'),
    ('timeChkM', '201307'),
    ('timeChkM', '201306'),
    ('timeChkM', '201305'),
    ('timeChkM', '201304'),
    ('timeChkM', '201303'),
    ('timeChkM', '201302'),
    ('timeChkM', '201301'),
    ('timeChkM', '201212'),
    ('timeChkM', '201211'),
    ('timeChkM', '201210'),
    ('timeChkM', '201209'),
    ('timeChkM', '201208'),
    ('timeChkM', '201207'),
    ('timeChkM', '201206'),
    ('timeChkM', '201205'),
    ('timeChkM', '201204'),
    ('timeChkM', '201203'),
    ('timeChkM', '201202'),
    ('timeChkM', '201201'),
    ('timeChkM', '201112'),
    ('timeChkM', '201111'),
    ('timeChkM', '201110'),
    ('timeChkM', '201109'),
    ('timeChkM', '201108'),
    ('timeChkM', '201107'),
    ('timeChkM', '201106'),
    ('timeChkM', '201105'),
    ('timeChkM', '201104'),
    ('timeChkM', '201103'),
    ('timeChkM', '201102'),
    ('timeChkM', '201101'),
    ('timeChkM', '201012'),
    ('timeChkM', '201011'),
    ('timeChkM', '201010'),
    ('timeChkM', '201009'),
    ('timeChkM', '201008'),
    ('timeChkM', '201007'),
    ('timeChkM', '201006'),
    ('timeChkM', '201005'),
    ('timeChkM', '201004'),
    ('timeChkM', '201003'),
    ('timeChkM', '201002'),
    ('timeChkM', '201001'),
    ('timeChkM', '200912'),
    ('timeChkM', '200911'),
    ('timeChkM', '200910'),
    ('timeChkM', '200909'),
    ('timeChkM', '200908'),
    ('timeChkM', '200907'),
    ('timeChkM', '200906'),
    ('timeChkM', '200905'),
    ('timeChkM', '200904'),
    ('timeChkM', '200903'),
    ('timeChkM', '200902'),
    ('timeChkM', '200901'),
    ('timeChkM', '200812'),
    ('timeChkM', '200811'),
    ('timeChkM', '200810'),
    ('timeChkM', '200809'),
    ('timeChkM', '200808'),
    ('timeChkM', '200807'),
    ('timeChkM', '200806'),
    ('timeChkM', '200805'),
    ('timeChkM', '200804'),
    ('timeChkM', '200803'),
    ('timeChkM', '200802'),
    ('timeChkM', '200801'),
    ('timeChkM', '200712'),
    ('timeChkM', '200711'),
    ('timeChkM', '200710'),
    ('timeChkM', '200709'),
    ('timeChkM', '200708'),
    ('timeChkM', '200707'),
    ('timeChkM', '200706'),
    ('timeChkM', '200705'),
    ('timeChkM', '200704'),
    ('timeChkM', '200703'),
    ('timeChkM', '200702'),
    ('timeChkM', '200701'),
]


def unsold_url(csv):
    url = f'https://kosis.kr/statHtml/downLarge.do?file={csv}'
    return url


UNSOLD_DOWN_HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://kosis.kr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://kosis.kr/statHtml/statHtml.do?orgId=116&tblId=DT_MLTM_2080&vw_cd=&list_id=&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=E1&docId=0317427997&markType=S&itmNm=%EC%A0%84%EA%B5%AD',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
}
UNSOLD_DOWN_COOKIES = {
    'newKOSIS2020StatisCtgrSettingCookie_1': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CI1%7CH2%7CN1%7CN2%7CT%7CU%7CK1%7CK2%7CJ1%7CJ2%7CL%7CM1%7CM2%7CO%7CO2%7CP%7CQ%7CR%7CS1%7CS2%7CI2%7CV',
    'mb': 'N',
    'JSESSIONID': 'EnL7qKu1dUa9sWANoarCunMr1Ko8iHEmxcZlMeTPO3wtw2T6JwUgaD7aVBnSh6KM.STAT_WAS1_servlet_engine5',
}
UNSOLD_DOWN_DATA = [
    ('orgId', '116'),
    ('tblId', 'DT_MLTM_2080'),
    ('language', 'ko'),
    ('file', ''),
    ('analText', ''),
    ('scrId', ''),
    ('fieldList',
     '[{"targetId":"PRD","targetValue":"","prdValue":"M,202102,202101,202012,202011,202010,202009,202008,202007,202006,202005,202004,202003,202002,202001,201912,201911,201910,201909,201908,201907,201906,201905,201904,201903,201902,201901,201812,201811,201810,201809,201808,201807,201806,201805,201804,201803,201802,201801,201712,201711,201710,201709,201708,201707,201706,201705,201704,201703,201702,201701,201612,201611,201610,201609,201608,201607,201606,201605,201604,201603,201602,201601,201512,201511,201510,201509,201508,201507,201506,201505,201504,201503,201502,201501,201412,201411,201410,201409,201408,201407,201406,201405,201404,201403,201402,201401,201312,201311,201310,201309,201308,201307,201306,201305,201304,201303,201302,201301,201212,201211,201210,201209,201208,201207,201206,201205,201204,201203,201202,201201,201112,201111,201110,201109,201108,201107,201106,201105,201104,201103,201102,201101,201012,201011,201010,201009,201008,201007,201006,201005,201004,201003,201002,201001,200912,200911,200910,200909,200908,200907,200906,200905,200904,200903,200902,200901,200812,200811,200810,200809,200808,200807,200806,200805,200804,200803,200802,200801,200712,200711,200710,200709,200708,200707,200706,200705,200704,200703,200702,200701,@"},{"targetId":"ITM_ID","targetValue":"13103792722T1","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0001","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0002","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0006","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0007","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0008","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0009","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0011","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0012","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0013","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0014","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0015","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0016","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0017","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0018","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"13102792722A.0019","prdValue":""},{"targetId":"OV_L2_ID","targetValue":"13102792722B.0001","prdValue":""},{"targetId":"OV_L2_ID","targetValue":"13102792722B.0002","prdValue":""},{"targetId":"OV_L2_ID","targetValue":"13102792722B.0003","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0001","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0002","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0003","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0004","prdValue":""},{"targetId":"OV_L3_ID","targetValue":"13102792722C.0005","prdValue":""}]'),
    ('colAxis', 'TIME,13101792722B,13101792722C'),
    ('rowAxis', '13101792722A'),
    ('isFirst', 'N'),
    ('contextPath', '/statHtml'),
    ('ordColIdx', ''),
    ('ordType', ''),
    ('logSeq', '106033059'),
    ('vwCd', ''),
    ('listId', ''),
    ('connPath', 'E1'),
    ('statId', '1998033'),
    ('pub', ''),
    ('pubLog', '4'),
    ('viewKind', '2'),
    ('viewSubKind', ''),
    ('doAnal', 'N'),
    ('analType', ''),
    ('analCmpr', ''),
    ('analTime', ''),
    ('analCombo', ''),
    ('originData', ''),
    ('analClass', ''),
    ('analItem', ''),
    ('obj_var_id', ''),
    ('itm_id', ''),
    ('mode', ''),
    ('dataOpt', 'ko'),
    ('noSelect', ''),
    ('view', 'csv'),
    ('existStblCmmtKor', 'Y'),
    ('existStblCmmtEng', 'N'),
    ('classAllArr',
     '[{"objVarId":"13101792722A","ovlSn":"1"},{"objVarId":"13101792722B","ovlSn":"2"},{"objVarId":"13101792722C","ovlSn":"3"}]'),
    ('classSet',
     '[{"objVarId":"13101792722A","ovlSn":"1","visible":"true"},{"objVarId":"13101792722B","ovlSn":"2","visible":"true"},{"objVarId":"13101792722C","ovlSn":"3","visible":"true"}]'),
    ('selectAllFlag', 'N'),
    ('selectTimeRangeCnt', '3'),
    ('periodStr', 'M'),
    ('funcPrdSe', ''),
    ('tblNm', '\uADDC\uBAA8\uBCC4 \uBBF8\uBD84\uC591\uD604\uD669'),
    ('tblEngNm', 'Unsold Housings by Size'),
    ('isChangedDataOpt', ''),
    ('itemMultiply', '285'),
    ('dimCo', '152'),
    ('dbUser', 'NSI.'),
    ('usePivot', 'N'),
    ('isChangedTableType', 'N'),
    ('isChangedPeriodCo', 'N'),
    ('isChangedPrdSort', 'N'),
    ('p_chkStatus', ''),
    ('p_objVarId', ''),
    ('p_lvl', ''),
    ('p_logicFlag', 'Y'),
    ('p_classAllChkYn', 'Y'),
    ('p_classAllSelectYn', 'N'),
    ('useAddFuncLog', ''),
    ('chargerLvl', ''),
    ('st', ''),
    ('new_win', ''),
    ('first_open', 'Y'),
    ('debug', ''),
    ('maxCellOver', ''),
    ('reqCellCnt', '855'),
    ('inheritYn', 'N'),
    ('originOrgId', ''),
    ('originTblId', ''),
    ('pubSeType', ''),
    ('relChkOrgId', ''),
    ('relChkTblId', ''),
    ('highLightStr',
     '[{"targetId":"PRD","targetValue":"202102","prdSe":"M"},{"targetId":"ITM","targetValue":"13103792722T1"},{"targetId":"VAL","val":"15,786","originVal":"15786"},{"targetId":"CLASS","value":{"objId1":"13101792722A","OV_L1_ID":"13102792722A.0001","objId2":"13101792722B","OV_L2_ID":"13102792722B.0001","objId3":"13101792722C","OV_L3_ID":"13102792722C.0001"},"classCnt":3}]'),
    ('markType', 'S'),
    ('docId', '3174'),
    ('itmNm', '\uC804\uAD6D'),
    ('tableType', 'default'),
    ('dataOpt2', 'ko'),
    ('periodCo', ''),
    ('enableLevelExpr', 'Y'),
    ('prdSort', 'desc'),
    ('findData', 'on'),
    ('compValue', ''),
    ('compValue01', ''),
    ('compValue02', ''),
    ('expDash', 'Y'),
    ('downGridFileType', 'xlsx'),
    ('downGridCellMerge', 'Y'),
    ('downGridMeta', 'Y'),
    ('downSort', 'asc'),
    ('pointType', 'screen'),
    ('downLargeFileType', 'csv'),
    ('downLargeExprType', '1'),
    ('downLargeSort', 'asc'),
    ('naviInfo', 'tabItemText'),
    ('naviInfo', '13101792722A'),
    ('naviInfo', '13101792722B'),
    ('naviInfo', '13101792722C'),
    ('naviInfo', 'tabTimeText'),
    ('itemChkLi', '13103792722T1'),
    ('classAllSelect', 'on'),
    ('classAllSelect', 'on'),
    ('classAllSelect', 'on'),
    ('classLvlAllChk1_1', 'on'),
    ('classChkLi1_1', '13102792722A.0001='),
    ('classChkLi1_1', '13102792722A.0002='),
    ('classChkLi1_1', '13102792722A.0003='),
    ('classChkLi1_1', '13102792722A.0004='),
    ('classChkLi1_1', '13102792722A.0005='),
    ('classChkLi1_1', '13102792722A.0006='),
    ('classChkLi1_1', '13102792722A.0007='),
    ('classChkLi1_1', '13102792722A.0008='),
    ('classChkLi1_1', '13102792722A.0009='),
    ('classChkLi1_1', '13102792722A.0010='),
    ('classChkLi1_1', '13102792722A.0011='),
    ('classChkLi1_1', '13102792722A.0012='),
    ('classChkLi1_1', '13102792722A.0013='),
    ('classChkLi1_1', '13102792722A.0014='),
    ('classChkLi1_1', '13102792722A.0015='),
    ('classChkLi1_1', '13102792722A.0016='),
    ('classChkLi1_1', '13102792722A.0017='),
    ('classChkLi1_1', '13102792722A.0018='),
    ('classChkLi1_1', '13102792722A.0019='),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('defaultFolder', '1'),
    ('classLvlAllChk2_1', 'on'),
    ('classChkLi2_1', '13102792722B.0001='),
    ('classChkLi2_1', '13102792722B.0002='),
    ('classChkLi2_1', '13102792722B.0003='),
    ('classLvlAllChk3_1', 'on'),
    ('classChkLi3_1', '13102792722C.0001='),
    ('classChkLi3_1', '13102792722C.0002='),
    ('classChkLi3_1', '13102792722C.0003='),
    ('classChkLi3_1', '13102792722C.0004='),
    ('classChkLi3_1', '13102792722C.0005='),
    ('headCheck', 'M'),
    ('timeChkM', '202102'),
    ('timeChkM', '202101'),
    ('timeChkM', '202012'),
    ('timeChkM', '202011'),
    ('timeChkM', '202010'),
    ('timeChkM', '202009'),
    ('timeChkM', '202008'),
    ('timeChkM', '202007'),
    ('timeChkM', '202006'),
    ('timeChkM', '202005'),
    ('timeChkM', '202004'),
    ('timeChkM', '202003'),
    ('timeChkM', '202002'),
    ('timeChkM', '202001'),
    ('timeChkM', '201912'),
    ('timeChkM', '201911'),
    ('timeChkM', '201910'),
    ('timeChkM', '201909'),
    ('timeChkM', '201908'),
    ('timeChkM', '201907'),
    ('timeChkM', '201906'),
    ('timeChkM', '201905'),
    ('timeChkM', '201904'),
    ('timeChkM', '201903'),
    ('timeChkM', '201902'),
    ('timeChkM', '201901'),
    ('timeChkM', '201812'),
    ('timeChkM', '201811'),
    ('timeChkM', '201810'),
    ('timeChkM', '201809'),
    ('timeChkM', '201808'),
    ('timeChkM', '201807'),
    ('timeChkM', '201806'),
    ('timeChkM', '201805'),
    ('timeChkM', '201804'),
    ('timeChkM', '201803'),
    ('timeChkM', '201802'),
    ('timeChkM', '201801'),
    ('timeChkM', '201712'),
    ('timeChkM', '201711'),
    ('timeChkM', '201710'),
    ('timeChkM', '201709'),
    ('timeChkM', '201708'),
    ('timeChkM', '201707'),
    ('timeChkM', '201706'),
    ('timeChkM', '201705'),
    ('timeChkM', '201704'),
    ('timeChkM', '201703'),
    ('timeChkM', '201702'),
    ('timeChkM', '201701'),
    ('timeChkM', '201612'),
    ('timeChkM', '201611'),
    ('timeChkM', '201610'),
    ('timeChkM', '201609'),
    ('timeChkM', '201608'),
    ('timeChkM', '201607'),
    ('timeChkM', '201606'),
    ('timeChkM', '201605'),
    ('timeChkM', '201604'),
    ('timeChkM', '201603'),
    ('timeChkM', '201602'),
    ('timeChkM', '201601'),
    ('timeChkM', '201512'),
    ('timeChkM', '201511'),
    ('timeChkM', '201510'),
    ('timeChkM', '201509'),
    ('timeChkM', '201508'),
    ('timeChkM', '201507'),
    ('timeChkM', '201506'),
    ('timeChkM', '201505'),
    ('timeChkM', '201504'),
    ('timeChkM', '201503'),
    ('timeChkM', '201502'),
    ('timeChkM', '201501'),
    ('timeChkM', '201412'),
    ('timeChkM', '201411'),
    ('timeChkM', '201410'),
    ('timeChkM', '201409'),
    ('timeChkM', '201408'),
    ('timeChkM', '201407'),
    ('timeChkM', '201406'),
    ('timeChkM', '201405'),
    ('timeChkM', '201404'),
    ('timeChkM', '201403'),
    ('timeChkM', '201402'),
    ('timeChkM', '201401'),
    ('timeChkM', '201312'),
    ('timeChkM', '201311'),
    ('timeChkM', '201310'),
    ('timeChkM', '201309'),
    ('timeChkM', '201308'),
    ('timeChkM', '201307'),
    ('timeChkM', '201306'),
    ('timeChkM', '201305'),
    ('timeChkM', '201304'),
    ('timeChkM', '201303'),
    ('timeChkM', '201302'),
    ('timeChkM', '201301'),
    ('timeChkM', '201212'),
    ('timeChkM', '201211'),
    ('timeChkM', '201210'),
    ('timeChkM', '201209'),
    ('timeChkM', '201208'),
    ('timeChkM', '201207'),
    ('timeChkM', '201206'),
    ('timeChkM', '201205'),
    ('timeChkM', '201204'),
    ('timeChkM', '201203'),
    ('timeChkM', '201202'),
    ('timeChkM', '201201'),
    ('timeChkM', '201112'),
    ('timeChkM', '201111'),
    ('timeChkM', '201110'),
    ('timeChkM', '201109'),
    ('timeChkM', '201108'),
    ('timeChkM', '201107'),
    ('timeChkM', '201106'),
    ('timeChkM', '201105'),
    ('timeChkM', '201104'),
    ('timeChkM', '201103'),
    ('timeChkM', '201102'),
    ('timeChkM', '201101'),
    ('timeChkM', '201012'),
    ('timeChkM', '201011'),
    ('timeChkM', '201010'),
    ('timeChkM', '201009'),
    ('timeChkM', '201008'),
    ('timeChkM', '201007'),
    ('timeChkM', '201006'),
    ('timeChkM', '201005'),
    ('timeChkM', '201004'),
    ('timeChkM', '201003'),
    ('timeChkM', '201002'),
    ('timeChkM', '201001'),
    ('timeChkM', '200912'),
    ('timeChkM', '200911'),
    ('timeChkM', '200910'),
    ('timeChkM', '200909'),
    ('timeChkM', '200908'),
    ('timeChkM', '200907'),
    ('timeChkM', '200906'),
    ('timeChkM', '200905'),
    ('timeChkM', '200904'),
    ('timeChkM', '200903'),
    ('timeChkM', '200902'),
    ('timeChkM', '200901'),
    ('timeChkM', '200812'),
    ('timeChkM', '200811'),
    ('timeChkM', '200810'),
    ('timeChkM', '200809'),
    ('timeChkM', '200808'),
    ('timeChkM', '200807'),
    ('timeChkM', '200806'),
    ('timeChkM', '200805'),
    ('timeChkM', '200804'),
    ('timeChkM', '200803'),
    ('timeChkM', '200802'),
    ('timeChkM', '200801'),
    ('timeChkM', '200712'),
    ('timeChkM', '200711'),
    ('timeChkM', '200710'),
    ('timeChkM', '200709'),
    ('timeChkM', '200708'),
    ('timeChkM', '200707'),
    ('timeChkM', '200706'),
    ('timeChkM', '200705'),
    ('timeChkM', '200704'),
    ('timeChkM', '200703'),
    ('timeChkM', '200702'),
    ('timeChkM', '200701'),
]
