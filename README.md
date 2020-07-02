# DataMiningTermp2

- Requirements
mlxend
numpy
pandas
pickle


설명
movleLens 25M 데이터에서 어떤 장르의 조합이 가장 성공을 거둘 수 있는지에 대해 연관규칙(Association Rule)을 이용하여 풀이해본 프로젝트입니다

Association Rule을 생성하기 위해 사용된 알고리즘은 Apriori, FP-Growth입니다.
(이에 대한 설명 http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/fpgrowth/)

자극적인 장르의 영화 매니아들을 추출하고

연관규칙으로 나온 장르들에 대해 매니아들준 평점과 Support, Confidence를 곱하는 식으로 간단한 성공지표를 계산하였습니다.

그 중 가장 높은 스코어를 기록한 2개 장르를 찾고

이 장르에는 어떤 영화가 있는지 확인하였습니다.

Apriori vs FP-Growth
Apriori : 테이블을 직접 순회하며 후보셋을 계속 생성해냅니다. 테이블을 계속 순회하기때문에 느립니다.
FP-Growth : linked-list 자료구조를 이용하기때문에 테이블을 2번만 순회합니다. 통상적으로 Apriori보다 빠르게 결과를 얻을 수 있습니다.

min_supprot에 걸리는 후보셋들이 많지 않은 경우 Apriori가 더 빠를 수 있습니다.
(ref : https://stackoverflow.com/questions/56651242/why-does-apriori-run-faster-than-fp-growth-in-this-implementation)
FP-Growth는 테이블을 반복적으로 순회하는 대신 task들을 쪼개서 탐색영역과 후보셋을 줄입니다.
단 min_support가 매우 낮은경우 FP-Tree에 많은 Branch들이 생성되고 이에 따라 overhead가 증가하면서 FP-Tree의 크기가 매우 커집니다
이 경우 매우 느리게 결과를 얻을 수 있습니다. 이를 피하기 위해서 projected database를 구축하는 것이 좋습니다.
