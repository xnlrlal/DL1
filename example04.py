import cv2 as cv      #opencv를 불러온다.

Path = 'C:/Users/rlatj/Desktop/DL1/data/'  # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
Name = 'HazyTown.jpg'       # 이용 할 사진

FullName = Path + Name      #가져올 이미지의 경로
img = cv.imread(FullName)       #이미지 가져오기

assert img is not None, "Failed to load image file.."       #img가 none인지 아닌지 테스트하고 없으면 "Failed to load image file.."출력.

img = img/255       #이미지 정규화.

def onChange(x):        #트랙바 이벤트 처리하는 콜백 함수.
    pass

cv.namedWindow('sigma_stregnth_setting')        #'sigma_stregnth_setting'라는 이름의 윈도우 생성
cv.createTrackbar('sigma', 'sigma_stregnth_setting', 0, 30, onChange)      #트랙바 생성 함수
cv.setTrackbarPos('sigma', 'sigma_stregnth_setting', 13)        #트랙바 초기값 설정
cv.createTrackbar('scale', 'sigma_stregnth_setting', 0, 10, onChange)      #트랙바 생성 함수
cv.setTrackbarPos('scale', 'sigma_stregnth_setting', 2)         #트랙바 초기값 설정

while True:
    sigma_change = cv.getTrackbarPos('sigma', 'sigma_stregnth_setting')     #시그마를 sigma_change라는 변수에 대입
    scale_change = cv.getTrackbarPos('scale', 'sigma_stregnth_setting')     #strength를 scale_change라는 변수에 대입

    if sigma_change!=sigma_change | scale_change!=scale_change:         #초기값과 변경된값이 다를때만 변경이되도록 설정
        k = sigma_change * 6 + 1        #k의 사이즈를 시그마*6+1로 설정
        um = img + scale_change * (img - cv.GaussianBlur(src=img, ksize=(k, k), sigmaX=sigma_change))       #um은 이미지+strength*(이미지-가우시안블러링해준값)해서 언샤프마스킹 실행.
        cv.imshow("sigma_stregnth_setting",um)      #언샤프마스킹한 값을 사진으로 출력.

    k = cv.waitKey(1) &0xFF     #waitkey를 27로 주어 esc를 누르면 while문에서 빠져나오게함.
    if k == 27:
        break

cv.destroyAllWindows()      #윈도우 종료
exit(0)