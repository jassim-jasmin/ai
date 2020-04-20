import urllib
import requests
import re
import json

imageServerIp = '192.168.15.65'
apiIp = '192.168.15.63'
county = 'SAN_DIEGO'
state = 'CA'
batchName = 'CASANDIEGO_20200323'
documentTypeOrg = 'deed'
imageList = ['SD-2020_00142235','SD-2020_00142182','SD-2020_00142601','SD-2020_00142512','SD-2020_00142214','SD-2020_00142174','SD-2020_00142168','SD-2020_00142175','SD-2020_00142163','SD-2020_00142435','SD-2020_00142433','SD-2020_00142372','SD-2020_00142153','SD-2020_00142147','SD-2020_00142146','SD-2020_00142135','SD-2020_00142126','SD-2020_00142593','SD-2020_00142605','SD-2020_00142413','SD-2020_00142213','SD-2020_00142178','SD-2020_00142149','SD-2020_00142587','SD-2020_00142484','SD-2020_00142184','SD-2020_00142177','SD-2020_00142166','SD-2020_00142155','SD-2020_00142555','SD-2020_00142520','SD-2020_00142483','SD-2020_00142442','SD-2020_00142429','SD-2020_00142361','SD-2020_00142345','SD-2020_00142343','SD-2020_00142238','SD-2020_00142362','SD-2020_00142359','SD-2020_00142426','SD-2020_00142424','SD-2020_00142410','SD-2020_00142622','SD-2020_00143087','SD-2020_00142953','SD-2020_00142697','SD-2020_00142658','SD-2020_00142660','SD-2020_00142993','SD-2020_00142949','SD-2020_00142934','SD-2020_00142912','SD-2020_00142641','SD-2020_00143049','SD-2020_00142900','SD-2020_00142828','SD-2020_00142629','SD-2020_00143102','SD-2020_00143067','SD-2020_00142894','SD-2020_00142832','SD-2020_00142655','SD-2020_00142645','SD-2020_00143036','SD-2020_00143015','SD-2020_00142995','SD-2020_00142860','SD-2020_00142853','SD-2020_00142794','SD-2020_00143081','SD-2020_00143048','SD-2020_00142895','SD-2020_00142889','SD-2020_00142695','SD-2020_00143014','SD-2020_00142910','SD-2020_00142880','SD-2020_00142892','SD-2020_00142891','SD-2020_00142893','SD-2020_00142774','SD-2020_00142937','SD-2020_00142816','SD-2020_00142815','SD-2020_00143621','SD-2020_00143609','SD-2020_00143599','SD-2020_00143275','SD-2020_00143606','SD-2020_00143600','SD-2020_00143499','SD-2020_00143485','SD-2020_00143397','SD-2020_00143395','SD-2020_00143378','SD-2020_00143314','SD-2020_00143264','SD-2020_00143207','SD-2020_00143380','SD-2020_00143288','SD-2020_00143282','SD-2020_00143272','SD-2020_00143268','SD-2020_00143269','SD-2020_00143204','SD-2020_00143203','SD-2020_00143200','SD-2020_00143448','SD-2020_00143337','SD-2020_00143336','SD-2020_00143319','SD-2020_00143298','SD-2020_00143611','SD-2020_00143598','SD-2020_00143517','SD-2020_00143500','SD-2020_00143503','SD-2020_00143401','SD-2020_00143400','SD-2020_00143270','SD-2020_00143616','SD-2020_00143604','SD-2020_00143594','SD-2020_00143511','SD-2020_00143515','SD-2020_00143513','SD-2020_00143433','SD-2020_00143428','SD-2020_00143149','SD-2020_00143592','SD-2020_00143519','SD-2020_00143293','SD-2020_00143279','SD-2020_00143285','SD-2020_00143289','SD-2020_00143267','SD-2020_00143623','SD-2020_00143505','SD-2020_00143432','SD-2020_00143427','SD-2020_00143246','SD-2020_00143389','SD-2020_00143436','SD-2020_00143406','SD-2020_00143399','SD-2020_00143358','SD-2020_00143521','SD-2020_00143496','SD-2020_00143493','SD-2020_00143441','SD-2020_00143403','SD-2020_00143459','SD-2020_00143445','SD-2020_00143444','SD-2020_00144012','SD-2020_00143974','SD-2020_00143949','SD-2020_00143879','SD-2020_00143864','SD-2020_00143840','SD-2020_00143841','SD-2020_00143830','SD-2020_00143820','SD-2020_00143753','SD-2020_00143752','SD-2020_00143743','SD-2020_00143710','SD-2020_00143717','SD-2020_00143715','SD-2020_00143718','SD-2020_00143671','SD-2020_00143663','SD-2020_00143648','SD-2020_00143642','SD-2020_00144123','SD-2020_00144069','SD-2020_00143882','SD-2020_00143804','SD-2020_00143784','SD-2020_00143721','SD-2020_00144112','SD-2020_00144107','SD-2020_00144079','SD-2020_00144114','SD-2020_00144100','SD-2020_00144085','SD-2020_00144044','SD-2020_00144042','SD-2020_00144030','SD-2020_00143998','SD-2020_00143965','SD-2020_00143953','SD-2020_00143887','SD-2020_00143876','SD-2020_00143832','SD-2020_00143839','SD-2020_00143837','SD-2020_00143833','SD-2020_00143792','SD-2020_00143780','SD-2020_00143741','SD-2020_00143697','SD-2020_00143645','SD-2020_00143629','SD-2020_00144064','SD-2020_00143878','SD-2020_00143822','SD-2020_00143796','SD-2020_00143798','SD-2020_00143791','SD-2020_00143785','SD-2020_00143776','SD-2020_00143728','SD-2020_00143737','SD-2020_00143652','SD-2020_00143639','SD-2020_00144082','SD-2020_00144014','SD-2020_00144000','SD-2020_00143874','SD-2020_00143805','SD-2020_00143794','SD-2020_00143683','SD-2020_00143660','SD-2020_00143656','SD-2020_00143628','SD-2020_00144105','SD-2020_00143928','SD-2020_00143694','SD-2020_00144103','SD-2020_00144090','SD-2020_00144053','SD-2020_00144040','SD-2020_00144031','SD-2020_00143993','SD-2020_00143991','SD-2020_00143827','SD-2020_00143803','SD-2020_00143799','SD-2020_00143789','SD-2020_00143696','SD-2020_00143669','SD-2020_00144062','SD-2020_00144058','SD-2020_00144001','SD-2020_00143977','SD-2020_00143960','SD-2020_00143942','SD-2020_00143919','SD-2020_00144115','SD-2020_00144120','SD-2020_00144049','SD-2020_00143999','SD-2020_00143963','SD-2020_00143971','SD-2020_00143934','SD-2020_00143893','SD-2020_00143881','SD-2020_00144109','SD-2020_00144023','SD-2020_00143983','SD-2020_00143980','SD-2020_00143868','SD-2020_00143771','SD-2020_00143712','SD-2020_00143699','SD-2020_00143689','SD-2020_00143688','SD-2020_00143748','SD-2020_00143701','SD-2020_00143691','SD-2020_00143870','SD-2020_00143871','SD-2020_00144088','SD-2020_00144068','SD-2020_00144056','SD-2020_00144553','SD-2020_00144556','SD-2020_00144547','SD-2020_00144454','SD-2020_00144467','SD-2020_00144461','SD-2020_00144465','SD-2020_00144447','SD-2020_00144340','SD-2020_00144282','SD-2020_00144279','SD-2020_00144247','SD-2020_00144128','SD-2020_00144566','SD-2020_00144557','SD-2020_00144560','SD-2020_00144508','SD-2020_00144442','SD-2020_00144426','SD-2020_00144411','SD-2020_00144407','SD-2020_00144379','SD-2020_00144252','SD-2020_00144245','SD-2020_00144187','SD-2020_00144185','SD-2020_00144171','SD-2020_00144439','SD-2020_00144431','SD-2020_00144416','SD-2020_00144409','SD-2020_00144377','SD-2020_00144345','SD-2020_00144336','SD-2020_00144320','SD-2020_00144287','SD-2020_00144125','SD-2020_00144131','SD-2020_00144132','SD-2020_00144437','SD-2020_00144421','SD-2020_00144412','SD-2020_00144385','SD-2020_00144322','SD-2020_00144309','SD-2020_00144312','SD-2020_00144316','SD-2020_00144302','SD-2020_00144169','SD-2020_00144135','SD-2020_00144503','SD-2020_00144514','SD-2020_00144474','SD-2020_00144288','SD-2020_00144300','SD-2020_00144256','SD-2020_00144253','SD-2020_00144250','SD-2020_00144198','SD-2020_00144188','SD-2020_00144151','SD-2020_00144156','SD-2020_00144552','SD-2020_00144541','SD-2020_00144507','SD-2020_00144473','SD-2020_00144481','SD-2020_00144472','SD-2020_00144424','SD-2020_00144414','SD-2020_00144404','SD-2020_00144315','SD-2020_00144305','SD-2020_00144307','SD-2020_00144289','SD-2020_00144152','SD-2020_00144216','SD-2020_00144209','SD-2020_00144191','SD-2020_00144182','SD-2020_00144174','SD-2020_00144160','SD-2020_00144539','SD-2020_00144464','SD-2020_00144405','SD-2020_00144325','SD-2020_00144222','SD-2020_00144179','SD-2020_00144158','SD-2020_00144555','SD-2020_00144492','SD-2020_00144167','SD-2020_00144165','SD-2020_00144554','SD-2020_00144532','SD-2020_00144535','SD-2020_00144499','SD-2020_00144399','SD-2020_00144521','SD-2020_00144520','SD-2020_00144513','SD-2020_00144522','SD-2020_00144523','SD-2020_00144545']
# imageList = ["SD-2020_00143081", "SD-2020_00144105", "SD-2020_00144556", "SD-2020_00144472","SD-2020_00144481"]

"""http://192.168.15.65/result_data/CA/SAN_DIEGO/CASANDIEGO_20200323/SD-2020_00142444/SD-2020_00142444.txt"""
etlUrlPath = 'http://' + imageServerIp + '//result_data//' + state + '//' + county + '//' + batchName + '//'
finalSourceTextLineWise = ''
#LINE WISE TEXT

def forGetFrom65():
    for tmpDirectory in imageList:
        # print(tmpDirectory)
        urlTextLineWise = etlUrlPath + tmpDirectory + '//' + tmpDirectory + '.txt'
        try:
            with urllib.request.urlopen(urlTextLineWise) as response:
                finalSourceTextLineWise = response.read().decode('utf-8')
        except Exception as e:
            print(e)

        predictionCountyName = re.sub('_','',county)
        predictionURL = 'http://'+apiIp+':6000/'+documentTypeOrg.lower()+'/?state='+state+'&county='+predictionCountyName
        fileContent = {'data':finalSourceTextLineWise}
        predictionResult = json.loads(requests.post(predictionURL,fileContent).text)

        # print(predictionResult.text)

        # jsonData = json.loads(predictionResult.text)

        # print(predictionResult["BUYER"])
        # print(predictionResult["SELLER"])

        buyer = predictionResult["BUYER"]
        seller = predictionResult["SELLER"]

        if len(buyer)>3:
            print(tmpDirectory + ':' + 'buyer', buyer)
        if len(seller)>3:
            print(tmpDirectory + ':' + 'seller', seller)

def forGetFrom63(url_l):
    try:
        result = {}
        seller_dic = dict()
        buyer_dic = dict()

        with urllib.request.urlopen(url_l) as response:
            # finalSourceTextLineWise = response.read().decode('utf-8')
            finalSourceTextLineWise = response.read()
            # print(finalSourceTextLineWise)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(finalSourceTextLineWise, 'html.parser')
            # print(soup)
            x = (soup.find_all('a'))


            for i in x:
                file_name = i.extract().get_text()
                print(file_name)

                urlTextLineWise = f'{url_l}{file_name}'
                # print(urlTextLineWise)

                try:
                    with urllib.request.urlopen(urlTextLineWise) as response:
                        finalSourceTextLineWise_main = response.read().decode('utf-8')
                        if len(finalSourceTextLineWise_main)<1000000:
                            # print(finalSourceTextLineWise_main)

                            predictionCountyName = re.sub('_', '', county)
                            predictionURL = 'http://' + apiIp + ':6000/' + documentTypeOrg.lower() + '/?state=' + state + '&county=' + predictionCountyName
                            fileContent = {'data': finalSourceTextLineWise_main}
                            predictionResult = json.loads(requests.post(predictionURL, fileContent).text)

                            buyer = predictionResult["BUYER"]
                            seller = predictionResult["SELLER"]
                            # print(predictionResult)

                            # if len(buyer) > 3:
                            #     print(file_name + ':' + 'buyer', buyer)
                            #     result['buyer'].apend(file_name)
                            # if len(seller) > 3:
                            #     print(file_name + ':' + 'seller', seller)
                            #     result['seller'].append(file_name)

                            seller_dic[file_name] = seller
                            buyer_dic[file_name] = buyer

                            result['seller'] = {"file": file_name, "data":seller}
                            result['buyer'] = {"file": file_name, "data":seller}
                        if len(finalSourceTextLineWise_main)>1000000:
                            print('Exceeed limit '+ file_name)

                        result['seller'] = seller_dic
                        result['buyer'] = buyer_dic

                        # return result # need to remove
                except Exception as e:
                    # print(e)
                    pass
        return result
    except Exception as e:
        print(e)

import time
start_time = time.time()

response = forGetFrom63('http://192.168.15.63/dataset/calosengeles/')

print("--- %s seconds ---" % (time.time() - start_time))
json_format = json.dumps(response)
fp = open('files/predicted_value_new.json', 'w')
fp.write(json_format)
##############################################

# [
#     "co - trustee robert m hanson aka rob hanson emudah- pbctebsr carolyn e murdock - pletcher aka carolyn murdock carolyn e murdock pletcher exempt trust created under the hanson family trust",
#     "co - trustee nai ? by counterparts e/ ) nae robert m hanson , aka rob hanson executed in counterparts curaten e murdeh- pbetebsr carolyn eb mordock - bletcher aka carolyn murdock carolyn e murdock pletcher exempt trust created under the hanson family trust agreement dated october 3 , 1989 ed in , counterparts wy ee puercleak - mister carolyn e murdock- pletcher , co - trustee + + + + + -----+++++rn el ce a sem pen dated september 17 , 2019 alchem properties , a joint venture y h & h investments , a general partnership by robert milo hanson exempt trust created under the hanson family trust agreement dated , october 3 , 1989 ee ee terparts by robert milo hanson , co - trustee by executed in counterparts mark freiburghouse co - trustee by hiatt family trust dated december 7 , 1995 a by cn william harrison jr hiatt , trustee the billings family trust",
#     "cynthia a billings , a co - trustee tenn mn on oe 7 ) anno garolyn e murdock - pletcher aka carolyn murdock ee ert a te nm ot cee at cee nema encom een pena tee a eam , et ta em tenth in tt rm carolyn e murdock pletcher exempt trust created under the hanson family trust",
#     "ie partnership bsaculrd ti , cc amparts robert milo hanson exempt trust created under the hanson family trust agreement dated october 3 , 1989 by foee 7 cta robert milo hanson , co - trustee by executed in counterparts mark freiburghouse co - trustee } i hiatt family trust dated december 7 , 1995 by executed in counterparts william harrison jr hiatt , trustee the billings family trust 7 06 - 14- 1989 } be bruce p billing co - trustee by ; executed in counterparts cynthia a billings , co - trustee executed jn counterparts ud vi eam ao robert m hanson , aka rob hanson cuted 4 , counterearts garolyn f ae -pletcher aka carolyn murdock carolyn e murdock pletcher - exempt trust - created under the hanson family trust agreement dates october 3 , by ecd jae a carolyn e murdock- -pletcher , , co - trustee by executed in counterparts mark freiburghouse , -co - trustee + + + + + -----+++++dated september 17 , 2019 alchem properties , a joint venture h & h investments , a general partnership by robert milo hanson exempt trust created under the hanson family trust",
#     "bru pe oe hy ee hy jo eh 4 ( fw jo soourr m aaa aka rob hanson executed in counterparts 3 ; 2 murctah- plcther carolyn e murdock - pletcher aka carolyn murdock carolyn e murdock pletcher exempt trust created under the hanson family trust agreement dares october 3 ecuted counterpar py chtebyn e- /paeeteck - veiher carolyn e murdock- pletcher , co - trustee by executed in counterparts mark freiburghouse"
# ]
