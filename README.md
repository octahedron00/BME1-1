# BME1-1
생명과학전공실험 1-1 실험 데이터 가공에 이용한 Python code

+ **모든 Python code는 2023년 3월 28일, 보고서 제출과 함께 업로드되었습니다.**

+ 용량 문제로 업로드 되지 않은 파일, BME1-1_TAIR10_GFF3.xlsx은 [이곳, TAIR10 사이트](https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_gff3/TAIR10_GFF3_genes_transposons.gff)에서 구할 수 있습니다.

+ 다운로드 후 excel에 붙여넣으면 됩니다.

## File list and explanation

### Methylation 데이터 가공

#### 제공된 data : 

+ Raw data = [BME1-1_Data.xlsx](/BME1-1_Data.xlsx)

+ TAIR10 data = BME1-1_TAIR10_GFF3.xlsx(용량 문제로 업로드되지 않음)

#### [BME1-1 t1.py](/BME1-1%20t1.py)

제공된 Raw data -> 각 methylation type 및 chromosome 별, 내부 100kbp 구간의 평균 데이터 형성

+ 데이터에 오류가 있는지 확인하기 위한 plot 형성

+ Excel output = [BME1-1_met_chr_100k.xlsx](/BME1-1_met_chr_100k.xlsx)

#### [BME1-1 t2.py](/BME1-1%20t2.py)

t1에서 형성한 data 바탕으로, Genome heatmap 형성

+ sns heatmap 이용, 이후 PPT 등으로 가공이 용이하도록 여백 및 크기 비율 조

#### [BME1-1 t3.py](/BME1-1%20t3.py)

> 직접적인 데이터 생성에는 이용하지 않음

각 methylation type에 따른 methylation 정도의 통계적 검정 진행

#### [BME1-1 t4.py](/BME1-1%20t4.py)

제공된 TAIR10 data -> gene, TE 정보만 추출하여, 각 염색체에 대해 '더 가벼운' 데이터 형성

+ Excel output = [BME1-1_Notation.xlsx](/BME1-1_Notation.xlsx)

#### [BME1-1 t5.py](/BME1-1%20t5.py)

t4의 데이터를 바탕으로, 제공된 Raw data의 각 window에 대해, 구성 요소 소속 여부를 확인하는 코드 작성

+ total, gene, promoter(gene 시작점 ~ upstream 1,000bp), transposable element

> 정렬된 두 data를 이용하기 때문에, 시간 복잡도는 O(L1 + L2)로 볼 수 있다. 정렬까지: O(L1 log L1 + L2 log L2)

+ Excel output = [BME1-1_met_chr_not.xlsx](/BME1-1_met_chr_not.xlsx)

#### [BME1-1 t6.py](/BME1-1%20t6.py)

t5의 데이터를 바탕으로, 각 methylation 데이터를 나타내는 plot 형성

+ 구성 요소 & methylation type을 바탕으로 plot 나눔

+ 각 plot 내 ecotype & 종자 단계별 data 추가

+ 모든 요소 대립에 대해 통계적으로 유의한 차이가 있는지 분석

+ Plot output = [Total.png](/Total.png) : 크기 문제로 output 유도

### 종자 단계 관찰 데이터 가공

#### [BME1-1 t7.py](/BME1-1%20t7.py)

실험 값에 대해, 유전형에 따라 각 단계 별로 관찰된 종자 수/비율 나타내는 plot 형성

#### [BME1-1 t8.py](/BME1-1%20t8.py)

실험 값에 대해, 카이제곱 검정 진행 후 결과 출력
