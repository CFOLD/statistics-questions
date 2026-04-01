## 1. Bayes 정리와 조건부확률

- 출제의 핵심은 `검사 정확도`와 `실제 양성 확률`이 서로 다르다는 점을 드러내는 데 있다. 학생이 민감도와 특이도를 posterior probability와 혼동하는지 가장 잘 드러나는 영역이다.
- 희귀질환, HIV, 진단장비, 반복 검사 같은 문맥을 주고 prior probability, true positive, false positive를 분리해 쓰게 하는 문항이 반복적으로 나온다.
- 한 번 양성인 경우와 두 번 연속 양성인 경우를 나누어 물으면, 같은 공식 암기 여부가 아니라 정보 갱신의 의미를 이해했는지 확인할 수 있다.
- 좋은 문항은 단순 숫자 답만 요구하지 않고, 왜 두 번째 결과에서 posterior가 더 커지는지, 혹은 왜 검사 정확도 99%가 곧 실제 양성 확률 99%가 아닌지를 설명하게 한다.
- 채점에서는 식을 세우는 과정, prior와 conditional probability의 역할 구분, 최종 수치, 그리고 문맥 해석을 분리해서 보는 것이 적절하다.
- 학생들은 특히 $P(H|+)$와 $P(+|H)$를 뒤바꾸고, 비감염자에 대한 정확도를 위양성률로 바꾸지 못하는 실수를 자주 한다. 따라서 각 항의 의미를 문장으로 설명하게 하는 장치가 필요하다.
- 반복 검사 문항에서는 첫 번째 사후확률을 두 번째 단계의 사전확률로 옮겨 적는 과정을 명시적으로 요구해야 한다. 이 단계가 빠지면 우연히 숫자만 맞는 답을 걸러내기 어렵다.
- 희귀질환 문항은 계산 뒤에 `얼마나 믿어야 하는가`를 해석하게 해야 한다. 직관과 posterior가 크게 어긋나는 이유를 설명하는 것이 핵심이다.

### 실제 문항

#### 문항 1

P(A) = 0.2, P(B) = 0.8 일때 다음에 대해서 답하시오 (총 10 점, 각 2.5 점)

**(a)** Can you compute $P(A \text{ and } B)$ if you only know $P(A)$ and $P(B)$?

**(b)** Assuming that events A and B arise from independent random processes, compute the followings.

- $P(A \text{ and } B) = ?$
- $P(A \text{ or } B) = ?$
- $P(A|B) = ?$

**(c)** If we are given that $P(A \text{ and } B) = 0.1$, are the random variables giving rise to events A and B independent?

**(d)** If we are given that $P(A \text{ and } B) = 0.1$, what is $P(A | B)$?

---

#### 해설

- (a) $P(A)$와 $P(B)$만으로는 $P(A\cap B)$를 정할 수 없다. 결합확률은 독립 여부나 추가 정보가 있어야 계산된다.
- (b) 독립이라고 했으므로
  $$P(A\cap B)=P(A)P(B)=0.2\times 0.8=0.16$$
  $$P(A\cup B)=P(A)+P(B)-P(A\cap B)=0.2+0.8-0.16=0.84$$
  $$P(A\mid B)=\frac{P(A\cap B)}{P(B)}=\frac{0.16}{0.8}=0.2$$
- (c) 독립이라면 $P(A\cap B)=P(A)P(B)=0.16$ 이어야 한다. 그런데 실제로 $0.1$이 주어졌으므로 독립이 아니다.
- (d)
  $$P(A\mid B)=\frac{P(A\cap B)}{P(B)}=\frac{0.1}{0.8}=0.125$$
  따라서 조건부확률은 `0.125`이다.

---


#### 문항 2

In a certain country, 2% of this country's population is infected with HIV. The ELISA test is one of the first and most accurate tests for HIV. For those who carry HIV, the ELISA test is 99% accurate. For those who do not carry HIV, the test is 90% accurate. If an individual from the country has tested positive, what is the probability that the individual carries HIV? (5 points)

---

#### 해설

- 사전확률은 $P(H)=0.02$, 음성이 아닌 사람의 확률은 $P(H^c)=0.98$ 이다.
- 민감도는 $P(+\mid H)=0.99$ 이고, 비감염자에게 90% 정확하다는 말은 위양성률이
  $$P(+\mid H^c)=1-0.90=0.10$$
  이라는 뜻이다.
- Bayes 정리를 적용하면
  $$
  P(H\mid +)=\frac{P(+\mid H)P(H)}{P(+\mid H)P(H)+P(+\mid H^c)P(H^c)}
  =\frac{0.99\cdot 0.02}{0.99\cdot 0.02+0.10\cdot 0.98}
  $$
  $$
  =\frac{0.0198}{0.1178}\approx 0.1681
  $$
- 따라서 양성 판정을 받았더라도 실제 감염 확률은 약 `16.81%`이다. 희귀질환에서는 검사 정확도가 높아도 posterior가 생각보다 낮을 수 있다는 점이 핵심이다.

---


#### 문항 3

Swaziland (아프리카의 한 국가) has the highest HIV prevalence in the world: 26% of this country's population is infected with HIV. The ELISA test is one of the first and most accurate tests for HIV. For those who carry HIV, the ELISA test is 99.7% accurate. For those who do not carry HIV, the test is 92.6% accurate. If an individual from Swaziland has tested positive, what is the probability that he carries HIV (5 점)?

---

#### 해설

- 주어진 값은 $P(H)=0.26$, $P(H^c)=0.74$, $P(+\mid H)=0.997$ 이다.
- 비감염자에 대한 정확도가 92.6% 이므로 위양성률은
  $$P(+\mid H^c)=1-0.926=0.074$$
- 따라서
  $$
  P(H\mid +)=\frac{0.997\cdot 0.26}{0.997\cdot 0.26+0.074\cdot 0.74}
  =\frac{0.25922}{0.25922+0.05476}
  =\frac{0.25922}{0.31398}
  \approx 0.8256
  $$
- 실제 감염 확률은 약 `82.56%`이다. 앞 문항과 달리 유병률이 매우 높기 때문에 양성 결과의 신뢰도가 크게 올라간다.

---


#### 문항 4

The same individual who tested positive tries to test again. Unfortunately, the individual has test positive again. What is the updated probability that he carries HIV (5 점)

---

#### 해설

- 첫 번째 양성 뒤의 사후확률을 두 번째 검사 전의 사전확률로 사용한다.
- 앞 문항에서
  $$P(H\mid +)\approx 0.8256,\qquad P(H^c\mid +)\approx 0.1744$$
- 같은 검사를 독립적으로 한 번 더 받았다고 보면
  $$
  P(H\mid ++)=\frac{0.997\cdot 0.8256}{0.997\cdot 0.8256+0.074\cdot 0.1744}
  $$
  $$
  =\frac{0.82312}{0.82312+0.01291}
  \approx 0.9846
  $$
- 따라서 두 번 연속 양성이면 실제 감염 확률은 약 `98.46%`가 된다.

---


#### 문항 5

In a certain country, 1% of this country's population is infected with HIV. For those who carry HIV, a certain test is 99% accurate. For those who do not carry HIV, the test is 90% accurate. (총 10 점)

1. 이 나라의 한 사람이 양성으로 검사되었다. 그가 진짜 HIV 를 가졌을 확률은? (3 점)
2. 이 사람이 다른 병원을 가서 동일 검사를 시행했는데 또 양성이 나왔다. 이 때 이 사람이 진짜 양성일 확률은? (3 점)
3. 위의 예를 사용하여 확률의 두가지 정의에 관하여 견해를 서술하시오 (4 점)

---

#### 해설

- 1회 양성일 때
  $$
  P(H\mid +)=\frac{0.99\cdot 0.01}{0.99\cdot 0.01+0.10\cdot 0.99}
  =\frac{0.0099}{0.1089}\approx 0.0909
  $$
  따라서 실제 양성일 확률은 약 `9.09%`이다.
- 2회 연속 양성일 때는 위 결과를 다시 prior로 두어
  $$
  P(H\mid ++)=\frac{0.99\cdot 0.0909}{0.99\cdot 0.0909+0.10\cdot 0.9091}
  \approx 0.4975
  $$
  따라서 두 번 모두 양성이면 실제 양성일 확률은 약 `49.75%`이다.
- 확률의 두 정의는 `빈도주의`와 `베이지안`이다. 빈도주의에서는 확률을 장기적 상대도수로 보고, 베이지안에서는 prior belief를 데이터로 갱신한 posterior probability로 본다. 이 문항은 같은 검사 결과도 prior에 따라 posterior가 크게 달라진다는 점을 보여 주는 전형적인 베이지안 예시다.

---


#### 문항 6

[5 점] Suppose that 1% of a country's population is infected with HIV. For those who carry HIV, there is a test that is 90% accurate. For those who do not carry HIV, the test is 80% accurate. If an individual from the country has tested positive, what is the probability that he carries HIV (2 점)?

The same individual who tested positive tries to test again. Unfortunately, the individual has test positive again. What is the updated probability that he carries HIV (3 점)?

---

#### 해설

- 주어진 값은 $P(H)=0.01$, $P(+\mid H)=0.90$, $P(+\mid H^c)=1-0.80=0.20$ 이다.
- 첫 번째 양성 posterior는
  $$
  P(H\mid +)=\frac{0.90\cdot 0.01}{0.90\cdot 0.01+0.20\cdot 0.99}
  =\frac{0.009}{0.207}\approx 0.0435
  $$
  즉 약 `4.35%`이다.
- 두 번째 양성까지 반영하면
  $$
  P(H\mid ++)=\frac{0.90\cdot 0.0435}{0.90\cdot 0.0435+0.20\cdot 0.9565}
  \approx 0.1698
  $$
  즉 약 `16.98%`이다.
- 검사 정확도가 앞 문항들보다 낮고 유병률도 낮기 때문에, 양성 결과가 나와도 실제 감염 확률은 여전히 높지 않다.

---


#### 문항 7

In a certain country, 1% of this country's population is infected with HIV. The ELISA test is one of the first and most accurate tests for HIV. For those who carry HIV, the ELISA test is 99% accurate. For those who do not carry HIV, the test is 90% accurate. If an individual from the country has tested positive, what is the probability that the individual carries HIV? (5 points) 이 사람이 다른 병원을 가서 동일 검사를 시행했는데 또 양성이 나왔다. 이때 이 사람이 진짜 양성일 확률은? (5 점) 위의 예를 들어 확률의 정의에 관한 두가지 견해를 서술하시오 (5 점)

---

#### 해설

- 계산은 문항 5와 같다.
  $$
  P(H\mid +)=\frac{0.99\cdot 0.01}{0.99\cdot 0.01+0.10\cdot 0.99}\approx 0.0909
  $$
  $$
  P(H\mid ++)=\frac{0.99\cdot 0.0909}{0.99\cdot 0.0909+0.10\cdot 0.9091}\approx 0.4975
  $$
- 따라서 첫 양성 후 실제 감염 확률은 약 `9.09%`, 두 번 연속 양성 후에는 약 `49.75%`이다.
- 빈도주의는 동일한 실험을 무한히 반복했을 때 사건이 일어나는 장기 비율로 확률을 해석한다. 베이지안은 관측 이전의 prior와 관측 데이터의 likelihood를 결합해 posterior를 구한다. 이 문항은 특히 posterior가 관측이 누적될수록 어떻게 바뀌는지를 보여 준다.

---


#### 문항 8

백만명중 한명이 걸리는 희귀병이 있다. 이를 진단하는 장비가 있는데 이 장비가 그 희귀병을 판단하는 정확도는 99% 이다. 이 장비를 사용하여 A 가 희귀병에 걸렸다는 진단을 내렸다. 이 사실을 얼마나 믿어야 하는가 베이지안 방법을 써서 예측하시오.

---

#### 해설

- 유병률이 백만 명 중 1명이므로
  $$P(H)=10^{-6},\qquad P(H^c)=1-10^{-6}$$
- 민감도와 특이도가 모두 99%라면
  $$P(+\mid H)=0.99,\qquad P(+\mid H^c)=0.01$$
- 따라서
  $$
  P(H\mid +)=\frac{0.99\cdot 10^{-6}}{0.99\cdot 10^{-6}+0.01\cdot (1-10^{-6})}
  $$
  $$
  \approx \frac{0.00000099}{0.01000098}\approx 0.000099
  $$
- 즉 실제로 병에 걸렸을 확률은 약 `0.0099%`에 불과하다. 양성 판정이 나와도 위양성의 절대 개수가 훨씬 많기 때문에, 이 결과를 그대로 믿기 어렵고 재검사가 필요하다고 해석하는 것이 맞다.


## 2. 이산확률모형, 기대값, 독립 시행

- 이 섹션은 이항분포, 기하분포, 독립 시행, 기대값, 공정 베팅, 카드/퀴즈/서브 같은 반복 시행 문항을 다룬다.
- 출제 포인트는 어떤 확률모형을 써야 하는지 식별하고, 정확한 사건 정의를 바탕으로 확률을 계산하게 하는 것이다.
- 예를 들어 `세 번째 성공이 열 번째에 일어나는가`, `정확히 몇 개를 맞추는가`, `평균적으로 몇 번 시도해야 하는가`, `기대값이 0이 되려면 얼마를 걸어야 하는가`는 서로 다른 사고를 요구한다.
- 좋은 문항은 같은 맥락 안에서 binomial, geometric, conditional probability를 구분하게 하여 학생이 사건 구조를 정말 이해했는지 드러내게 한다.
- 또한 독립인 비용이나 물량의 합에 대해 평균과 표준편차를 계산하게 하는 문항은 분포 선택보다 선형성, 분산 합산, 독립 가정을 점검하는 데 효과적이다.
- 실제 출제에서는 `이 문제가 어떤 분포 문제인지`를 식별하는 능력이 중요하다. 성공 횟수인지, 첫 성공까지의 시행 수인지, 독립인 합의 평균과 분산인지 구분하게 해야 한다.
- 채점은 정답 수치만 보면 안 되고, 사건 정의를 올바르게 잡았는지, 조합식을 쓰는지 순서를 쓰는지, 기대값과 공정 베팅을 같은 것으로 착각하지 않았는지를 따로 봐야 한다.
- 자주 나오는 오답은 `정확히 k개`와 `최초 성공이 k번째`를 혼동하거나, 독립 시행의 조건부 상황에서도 이전 결과가 다음 성공확률을 바꾼다고 오해하는 경우다. 이런 오개념은 설명형 소문항을 같이 두면 잘 드러난다.
- 기대값 문항은 계산만 맞으면 끝이 아니라 `그래서 이 게임을 해야 하는가`, `공정한 금액은 얼마인가`까지 문맥 판단을 붙이는 것이 좋다. 숫자를 행동 판단으로 번역하는 능력이 여기서 갈린다.
- 공정 베팅 문항은 기대값이 0이 되도록 식을 세우는지를 보는 가장 짧은 진단 문제다. 이때 학생이 누구의 승리 때 얼마를 얻고 잃는지 부호를 바꾸는 실수가 많으므로, 기대이익 식 자체를 채점 항목으로 분리하는 것이 좋다.
- 비용 합산 문항은 평균의 선형성과 분산의 가법성을 구분하게 해야 한다. 평균은 바로 더하지만 표준편차는 직접 더하지 않는다는 점을 서술하게 하면 계산 실수를 크게 줄일 수 있다.
- 반복 시행 문항은 `정확히 k개 성공`, `r번째 성공이 k번째 시행에서 나옴`, `이미 일부 결과가 주어진 뒤 다음 1회 성공확률`을 의도적으로 분리해 묻는 편이 좋다. 그래야 학생이 binomial, negative binomial/geometric, 조건부확률을 구별하는지 드러난다.

### 실제 문항

---


#### 문항 1

You and your friend decide to bet on the Major League Baseball game happening one evening between the Los Angeles Dodgers and the San Diego Padres. Suppose current statistics indicate that the Dodgers have a 0.40 probability of winning this game against the Padres. If your friend bets you $5 that the Dodgers will win, how much would you need to bet on the Padres to make this a fair game? (5 점)

---

#### 해설

- 내가 Padres에 $x$달러를 걸었다고 하자.
- Padres가 이길 확률은 `0.60`, 이때 친구에게서 `$5`를 받는다. Dodgers가 이길 확률은 `0.40`, 이때 내가 `$x`를 잃는다.
- 공정한 게임은 기대이익이 0인 경우이므로
  $$
  E(\text{profit})=0.60(5)+0.40(-x)=0
  $$
  $$
  3-0.4x=0 \Rightarrow x=7.5
  $$
- 따라서 Padres 쪽에 `$7.50`을 걸어야 공정하다.

---


#### 문항 2

You and your friend decide to bet on the Major League Baseball game happening one evening between the Los Angeles Dodgers and the San Diego Padres. Suppose current statistics indicate that the Dodgers have a 0.54 probability of winning this game against the Padres. If your friend bets you $10 that the Dodgers will win, how much would you need to bet on the Padres to make this a fair game (5 점)?

---

#### 해설

- 이번에는 Dodgers 승리확률이 `0.54`이므로 Padres 승리확률은 `0.46`이다.
- Padres가 이기면 친구에게서 `$10`을 받고, Dodgers가 이기면 내가 `$x`를 잃는다.
- 공정 베팅 조건:
  $$
  0.46(10)+0.54(-x)=0
  $$
  $$
  4.6-0.54x=0 \Rightarrow x=\frac{4.6}{0.54}\approx 8.52
  $$
- 따라서 내가 Padres에 걸 금액은 약 `$8.52`여야 한다.

---


#### 문항 3

어떤 택배기사는 일주일에 5 일 배송을 한다. 그가 매일 배송하는 물건은 random 하고 independently 하게 배정된다고 한다. 그는 하루에 평균 40 개를 배송하고 표준편차는 4 개이다. 그가 일주일 (5 일) 간 배달하는 총 물건의 평균 갯수와 표준편차는 얼마인가? (5 점)

---

#### 해설

- 하루 배송 수를 $X_i$라 하면 $E(X_i)=40$, $SD(X_i)=4$, 따라서 $Var(X_i)=16$이다.
- 일주일 총 배송 수를 $T=X_1+\cdots+X_5$ 라 두면 독립이므로
  $$
  E(T)=\sum E(X_i)=5\times 40=200
  $$
  $$
  Var(T)=\sum Var(X_i)=5\times 16=80
  $$
  $$
  SD(T)=\sqrt{80}\approx 8.94
  $$
- 따라서 평균은 `200개`, 표준편차는 약 `8.94개`이다.

---


#### 문항 4

어떤 회사원은 출근하면서 커피 한잔과 머핀빵 하나를 매일 아침으로 사먹는다. 그는 근처의 여러 커피점에서 random 하고 independently 하게 커피와 머핀빵을 선택한다고 한다. 그가 사먹는 커피 한잔의 평균가격은 3,000 원이고 표준편차는 500 원이다. 머핀빵은 평균가격이 3,000 원 이고 표준편차는 1,000 원이다. 이 때 다음을 계산하시오 (각 2 점, 총 4 점)

(a) 그가 매일 아침으로 지출하는 금액의 평균과 표준편차는 얼마인가?

(b) 그가 매주 평일 아침 (주 5 일) 로 지출하는 금액의 평균과 표준편차는 얼마인가?

---

#### 해설

- 하루 커피 가격을 $C$, 머핀 가격을 $M$이라 하자.
- 평균은 더하면 되므로
  $$
  E(C+M)=E(C)+E(M)=3000+3000=6000
  $$
- 독립이므로 분산도 더할 수 있다.
  $$
  Var(C+M)=500^2+1000^2=250000+1000000=1250000
  $$
  $$
  SD(C+M)=\sqrt{1250000}\approx 1118.03
  $$
- 5일 총지출을 $W$라 하면
  $$
  E(W)=5\times 6000=30000
  $$
  $$
  Var(W)=5\times 1250000=6250000,\qquad SD(W)=\sqrt{6250000}=2500
  $$
- 따라서 하루 기준 평균 `6000원`, 표준편차 약 `1118.03원`, 5일 기준 평균 `30000원`, 표준편차 `2500원`이다.

---


#### 문항 5

[4 점] 영희는 매일 아침 동네에 있는 여러 커피가게 중 한 가게에서 커피 한잔과 머핀 하나를 사먹는다. 영희는 매일 이전과는 독립적으로 랜덤하게 커피가게를 고른다고 한다. 커피의 평균가격은 3,000 원 이고 표준편차는 1,000 원 이며 머핀은 평균가격 3,000 원 표준편차는 500 원이라 한다. 이때 커피와 머핀 가격은 각각 독립이라 가정한다.

(a) 영희가 매일 아침 커피가게에서 쓰는 비용의 평균값과 표준편차는 얼마인가?  
(b) 영희가 평일 5 일 동안 쓰는 비용의 평균값과 표준편차는 얼마인가?

---

#### 해설

- 하루 평균은 여전히
  $$3000+3000=6000$$
- 하루 분산은 이번에는
  $$
  1000^2+500^2=1000000+250000=1250000
  $$
  이므로 표준편차는
  $$
  \sqrt{1250000}\approx 1118.03
  $$
- 5일 합에 대해서는
  $$
  E(W)=5\times 6000=30000,\qquad Var(W)=5\times 1250000=6250000
  $$
  $$
  SD(W)=\sqrt{6250000}=2500
  $$
- 따라서 문항 4와 숫자가 같고, 그 이유는 표준편차의 순서가 바뀌었을 뿐 분산의 합이 동일하기 때문이다.

---


#### 문항 6

A volleyball player has an 80% chance of making the serve (배구 서비스 성공률). Suppose that her serves are independent of each other. (총 5 점)

(a) What is the probability that on the 4th try she will make her 3rd successful serve?

(b) Suppose she has made two successful serves in three attempts. What is the probability that her 4th serve will be successful?

(c) (a) 와 (b) 의 값이 다른가? 다르다면 이유를 설명하시오.

---

#### 해설

- (a) 4번째 시도에서 3번째 성공이 나오려면, 처음 3번 중 정확히 2번 성공하고 4번째도 성공해야 한다.
  $$
  P=\binom{3}{2}(0.8)^2(0.2)(0.8)=\binom{3}{2}(0.8)^3(0.2)=0.3072
  $$
- (b) 이미 3번 중 2번 성공했다는 사실이 주어져도, 서비스들이 독립이므로 4번째 성공확률은 그대로
  $$P(\text{4th success}\mid \text{first 3 results})=0.8$$
- (c) (a)는 특정 경로 전체의 확률이고, (b)는 주어진 조건 아래 마지막 1회의 성공확률이다. 따라서 두 값이 다르다.

---


#### 문항 7

In a multiple choice quiz there are 5 questions and 5 choices for each question (a, b, c, d, e). Robin has not studied for the quiz at all, and decides to randomly guess the answers. (총 5 점) What is the probability that

**(a)** the first question she gets right is the 3rd question?

**(b)** she gets exactly 3 or exactly 4 questions right?

**(c)** she gets the majority of the questions right?

---

#### 해설

- 각 문항 정답확률은 $p=1/5=0.2$, 오답확률은 $0.8$이다.
- (a) 첫 정답이 3번째라는 말은 처음 두 문제를 틀리고 세 번째를 맞히는 경우이므로
  $$
  0.8^2\times 0.2=0.128
  $$
- (b) 정확히 3개 또는 4개 정답 확률은
  $$
  P(X=3)+P(X=4)=\binom53(0.2)^3(0.8)^2+\binom54(0.2)^4(0.8)
  $$
  $$
  =10(0.008)(0.64)+5(0.0016)(0.8)=0.0512+0.0064=0.0576
  $$
- (c) 과반수 정답은 3개 이상 정답이므로
  $$
  P(X\ge 3)=P(X=3)+P(X=4)+P(X=5)
  $$
  $$
  =0.0512+0.0064+(0.2)^5=0.0512+0.0064+0.00032=0.05792
  $$

---


#### 문항 8

A certain survey estimates that 2/3 (two third) of women ages 20 years and over are married. (5 점)

1. We randomly select three women of these ages. What is the probability that the third woman selected is the only one who is married?
2. What is the probability that all three randomly selected women are married?
3. On average, how many women would you expect to sample before selecting a married woman? What is the standard deviation?
4. If the proportion of married women was actually 1/3 (one third), how many women would you expect to sample before selecting a married woman? What is the standard deviation?

---

#### 해설

- 기혼 확률을 $p=2/3$, 미혼 확률을 $q=1/3$라 하자.
- 1) 세 번째 여성이 유일한 기혼자라는 뜻은 앞의 두 명은 미혼, 세 번째만 기혼이라는 뜻이므로
  $$
  q^2p=\left(\frac13\right)^2\left(\frac23\right)=\frac{2}{27}\approx 0.07407
  $$
- 2) 세 명 모두 기혼일 확률은
  $$
  p^3=\left(\frac23\right)^3=\frac{8}{27}\approx 0.29630
  $$
- 3) 첫 기혼자를 만날 때까지의 표본 수를 geometric 분포로 보면
  $$
  E(X)=\frac1p=\frac{3}{2}=1.5,\qquad SD(X)=\frac{\sqrt{1-p}}{p}=\frac{\sqrt{1/3}}{2/3}\approx 0.8660
  $$
- 4) 만약 $p=1/3$이면
  $$
  E(X)=\frac1{1/3}=3,\qquad SD(X)=\frac{\sqrt{2/3}}{1/3}=\sqrt{6}\approx 2.4495
  $$

---


#### 문항 9

A not-so-skilled volleyball player has a 25% chance of making the serve, which involves hitting the ball so it passes over the net on a trajectory such that it will land in the opposing team's court. Suppose that her serves are independent of each other. (총 15 점, 각 5 점)

**(a)** What is the probability that on the 10th try she will make her 3rd successful serve?

**(b)** Suppose she has made two successful serves in nine attempts. What is the probability that her 10th serve will be successful?

**(c)** Even though parts (a) and (b) discuss the same scenario, the probabilities you calculated should be different. Can you explain the reason for this discrepancy?

---

#### 해설

- (a) 10번째 시도에서 3번째 성공이 나오려면, 앞의 9번 중 정확히 2번 성공하고 10번째를 성공해야 한다.
  $$
  P=\binom92(0.25)^2(0.75)^7(0.25)=\binom92(0.25)^3(0.75)^7
  $$
  $$
  =36(0.015625)(0.1334839)\approx 0.07508
  $$
- (b) 이미 9번 중 2번 성공했다는 사실이 주어지면, 독립성 때문에 10번째 성공확률은 그대로
  $$0.25$$
- (c) (a)는 10번 전체 시행 경로가 일어날 확률이고, (b)는 앞 9번 결과가 이미 주어진 뒤 마지막 한 번의 성공확률이다. 따라서 값이 다르게 나오는 것이 맞다.

---


#### 문항 10

In a new card game, you start with a well-shuffled full deck and draw 3 cards without replacement. If you draw 3 hearts, you win $100. If you draw 3 black cards, you win $50. For any other draws, you win nothing (총 10 점).

**(a)** Create a probability model for the amount you win at this game, and find the expected winnings. Also compute the standard deviation of this distribution.

**(b)** If the game costs $10 to play, what would be the expected value of the net profit (or loss)? (Hint: profit = winnings - cost; $X - 10$) Should you play this game? Explain.

---

#### 해설

- 52장 카드 중 하트는 13장, 검은 카드는 26장이다.
- 3장 모두 하트일 확률:
  $$
  P(X=100)=\frac{\binom{13}{3}}{\binom{52}{3}}=\frac{286}{22100}\approx 0.01294
  $$
- 3장 모두 검은 카드일 확률:
  $$
  P(X=50)=\frac{\binom{26}{3}}{\binom{52}{3}}=\frac{2600}{22100}\approx 0.11765
  $$
- 나머지는
  $$
  P(X=0)=1-0.01294-0.11765=0.86941
  $$
- 기대값은
  $$
  E(X)=100(0.01294)+50(0.11765)=1.294+5.8825=7.1765
  $$
- 제곱의 기대값은
  $$
  E(X^2)=100^2(0.01294)+50^2(0.11765)=129.4+294.125=423.525
  $$
  따라서
  $$
  Var(X)=E(X^2)-[E(X)]^2=423.525-(7.1765)^2\approx 371.03
  $$
  $$
  SD(X)\approx \sqrt{371.03}\approx 19.29
  $$
- 참가비 10달러를 빼면 기대 순이익은
  $$E(X-10)=7.1765-10=-2.8235$$
  이므로 기대값 기준으로는 하지 않는 편이 낫다.


## 3. 기술통계, 시각화, 분포 형태 해석

- 이 섹션은 histogram, box plot, five-number summary, 왜도, mean vs median, SD vs IQR, robustness를 중심으로 출제한다.
- 핵심은 값을 기계적으로 요약하는 것이 아니라, 어떤 자료의 중심과 퍼짐을 어떤 통계량으로 대표하는 것이 더 적절한지 이유와 함께 판단하게 하는 데 있다.
- 우측 왜도, 극단값, 다봉성, 긴 꼬리 같은 특징이 있을 때 mean/SD 대신 median/IQR를 고르게 하는 문제는 가장 전형적이며 설명형 채점이 쉽다.
- 점수표, 집값, 음주량, 급여처럼 익숙한 자료를 제시하고 실제로 histogram이나 box plot을 그리게 하면 통계량의 의미를 시각적으로 이해했는지를 볼 수 있다.
- 채점에서는 그림의 정확성뿐 아니라, 선택한 요약통계가 왜 그 분포에 맞는지 설득력 있게 설명했는지를 같이 봐야 한다.
- 좋은 출제는 그림을 그리게 한 뒤 바로 끝내지 않고, `왜 이 분포를 left/right skew 혹은 symmetric로 보는가`, `왜 mean보다 median이 더 적절한가`까지 언어로 쓰게 해야 한다.
- 학생들은 종종 outlier 하나만 보고 무조건 right skew라고 하거나, median과 mean의 상대적 위치를 반대로 기억한다. 따라서 분포 특징과 대표값 선택을 함께 묶어 묻는 구성이 효과적이다.
- 박스플롯 문항에서는 fence 계산, mild outlier 여부, IQR의 강건성까지 자연스럽게 연결할 수 있다. 단순 그림 재현보다 요약값 해석을 포함하는 편이 낫다.
- 채점은 `형태 판정`, `대표 중심 선택`, `대표 퍼짐 선택`, `그 이유`의 네 단계로 나누는 것이 좋다. 특히 이유가 없는 답은 부분점수만 주는 기준이 적절하다.

### 실제 문항

---


#### 문항 1

Below are the final scores of 20 introductory statistics students. Draw a histogram of these data and describe the distribution (5 점).

79, 83, 57, 82, 94, 83, 72, 74, 73, 71, 66, 89, 78, 81, 78, 81, 88, 69, 77, 79

---

#### 해설

- 주어진 점수들은 전체적으로 `70점대 후반`을 중심으로 모여 있고, 뚜렷한 봉우리가 하나 보이는 단봉형 분포로 해석할 수 있다.
- 다만 57점이 다른 점수들보다 상대적으로 낮아 왼쪽 꼬리를 약간 길게 만들기 때문에, 완전히 대칭이라고 보기보다는 `약한 left skew` 또는 낮은 값 쪽으로 꼬리가 조금 늘어진 분포라고 설명하는 것이 적절하다.
- 이런 분포에서는 평균과 중앙값이 아주 크게 다르지는 않겠지만, 낮은 극단값 하나가 평균을 조금 끌어내릴 수 있다는 점도 함께 언급하면 더 좋은 답안이 된다.

---


#### 문항 2

Create a box plot for the data given in Prob. #1. The five number summary provided below may be useful (5 점).

| Min | Q1 | Q2 (Median) | Q3 | Max |
|-----|----|-------------|----|-----|
| 57 | 72.5 | 78.5 | 82.5 | 94 |

---

#### 해설

- 주어진 five-number summary를 이용하면 $IQR=Q_3-Q_1=82.5-72.5=10$ 이다.
- box plot에서 outlier 여부를 판단할 때 하한 fence는 $Q_1-1.5\times IQR=72.5-15=57.5$ 가 된다.
- 실제 최솟값은 57이므로 이 값은 하한 fence보다 조금 작다. 따라서 57점은 낮은 쪽 `mild outlier`로 표시하는 것이 적절하다.
- 중앙값은 78.5로 상자 중앙 부근에 있고, 나머지 자료는 비교적 고르게 분포해 있으므로 전체 box plot은 대체로 균형적이지만 왼쪽 끝에 약한 이상치가 하나 있는 형태로 그리면 된다.

---


#### 문항 3

For each of the following, describe whether you expect the distribution to be symmetric, right skewed, or left skewed. Also specify whether the mean or median would best represent a typical observation in the data, and whether the variability of observations would be best represented using the standard deviation or IQR. 이유를 설득력있도록 쓰시오. (각 2.5 점, 총 10 점)

**(a)** Housing prices in a country where 25% of the houses cost below $350,000, 50% of the houses cost below $450,000, 75% of the houses cost below $1,000,000 and there are a meaningful number of houses that cost more than $6,000,000.

**(b)** Housing prices in a country where 25% of the houses cost below $300,000, 50% of the houses cost below $600,000, 75% of the houses cost below $900,000 and very few houses that cost more than $1,200,000.

**(c)** Number of alcoholic drinks consumed by college students in a given week.

**(d)** 국내 대기업에 다니는 직원의 봉급

---

#### 해설

- (a) 고가 주택 몇 채가 매우 큰 값을 만들어 오른쪽 꼬리를 길게 끌기 때문에 `right skew`이다. 이런 경우 평균은 극단값의 영향을 크게 받으므로 중심은 `median`, 퍼짐은 `IQR`로 요약하는 것이 적절하다.
- (b) 사분위수가 비교적 고르게 퍼져 있고 극단적으로 큰 집이 매우 많지 않으므로 대체로 `symmetric`에 가깝다고 볼 수 있다. 이런 경우 중심은 `mean`, 퍼짐은 `SD`가 자연스럽다.
- (c) 대학생의 주간 음주량은 0 또는 소량 음주자가 많고, 소수의 과음자가 큰 값을 만들 가능성이 높다. 따라서 `right skew`로 보고 대표 중심은 `median`, 대표 퍼짐은 `IQR`을 쓰는 것이 مناسب하다.
- (d) 대기업 직원의 봉급도 소수의 고연봉자가 분포 오른쪽 꼬리를 길게 만들 가능성이 높다. 따라서 `right skew`로 보고 중심은 `median`, 퍼짐은 `IQR`을 선택하는 것이 설득력 있다.


## 4. 정규분포, 표본분포, 중심극한정리

- 정규분포 자체의 확률 계산과 표본평균의 분포를 구분해서 다루는 것이 중요하다. 학생이 모집단 분포와 sampling distribution을 혼동하는 경우가 많다.
- 중심극한정리는 정의만 암기하게 할 것이 아니라, 왜 가설검정과 신뢰구간의 이론적 배경이 되는지까지 설명하게 해야 출제 효과가 있다.
- 동전이나 질병처럼 이산 자료가 아니라 연속 자료의 평균이 정규근사되는 이유, 표본 수가 커질수록 표본평균의 분포가 어떻게 바뀌는지를 묻는 서술형이 적합하다.
- 좋은 문항은 `개별 관측치의 분포`와 `표본평균의 분포`를 같은 축에서 비교시키고, 평균은 같지만 표준편차가 어떻게 줄어드는지 스스로 말하게 한다.
- 이 영역은 계산형과 설명형을 섞을수록 좋다. z 계산만 내기보다 CLT의 역할을 언어로 정리하게 해야 한다.
- 출제의 변별점은 학생이 $\sigma$ 와 $\sigma/\sqrt{n}$ 을 언제 쓰는지 정확히 구분하는가에 있다. 같은 2.4라는 기준값이라도 개별 관측치와 표본평균에서 확률이 극적으로 달라진다는 점을 드러내는 문항이 좋다.
- CLT 문항은 단순 정의 암기보다 `왜 모집단이 정규가 아니어도 평균에 대한 추론이 가능해지는가`를 설명하게 해야 한다. 이 설명이 되면 이후 신뢰구간과 가설검정 이해가 안정적이다.
- 학생들은 모집단이 정규여야만 CLT를 쓸 수 있다고 오해하거나, 표본 자체가 정규분포를 따른다고 착각하는 경우가 많다. 참/거짓형이나 비교형으로 이 오개념을 따로 확인하면 좋다.
- 채점에서는 계산 정확도와 함께 `분포의 이름`, `평균`, `표준오차`, `근사 논리`를 각각 봐야 한다.

### 실제 문항

---


#### 문항 1

The distribution of weights of US pennies is approximately normal with a mean of 2.5 grams and a standard deviation of 0.025 grams. (총 10 점)

**(a)** What is the probability that a randomly chosen penny weighs less than 2.4 grams?

**(b)** Describe the sampling distribution of the mean weight of 10 randomly chosen pennies.

**(c)** What is the probability that the mean weight of 10 pennies is less than 2.4 grams?

**(d)** Sketch the two distributions (population and sampling) on the same scale.

---

#### 해설

- 개별 관측치에 대해 $z=(2.4-2.5)/0.025=-4$이므로 확률은 약 $3.17 \times 10^{-5}$.
- 표본평균 분포의 평균은 `2.5`, 표준편차는 `0.025/\sqrt{10}\approx 0.00791`.
- 표본평균이 2.4보다 작을 확률은 사실상 `0`이다.
- 두 분포의 평균은 같고 표본평균 분포가 더 좁다.

---


#### 문항 2

"중심극한정리"가 왜 통계학에서 중요한지 모집단 분포와의 관계를 들어 자세하게 설명하시오

---

#### 해설

- 중심극한정리는 통계학에서 매우 중요한 정리인데, 이유는 모집단 분포가 꼭 정규분포가 아니더라도 표본 크기가 충분히 크면 `표본평균의 분포`가 정규분포에 가까워지기 때문이다.
- 즉, 원자료 자체가 비대칭이거나 이상치를 조금 포함하더라도, 평균이라는 통계량은 반복 표집을 생각했을 때 훨씬 더 안정적이고 정규적인 형태를 보이게 된다.
- 이 성질 덕분에 우리는 모집단 분포를 완전히 알지 못해도 평균에 대한 신뢰구간을 만들고, 평균 차이에 대한 가설검정을 수행할 수 있다.
- 따라서 중심극한정리는 단순한 분포 성질이 아니라, 추론통계 전체를 가능하게 해 주는 핵심 이론적 기반이라고 설명할 수 있다.

---


#### 문항 3

[5 점] 중심극한정리는 가설검정의 이론적 배경을 제공한다. 다음에 대하여 서술하시오.

1. 중심극한정리의 정의를 정확하게 쓰고
2. 이것이 왜 가설검정의 배경을 제공하는지 설명하시오

---

#### 해설

- 중심극한정리의 정의는, 독립이고 동일한 분포를 따르는 표본을 충분히 크게 뽑으면 표본평균의 분포가 평균 $\mu$, 분산 $\sigma^2/n$인 정규분포에 가까워진다는 것이다.
- 여기서 중요한 점은 `개별 관측값`이 아니라 `표본평균`의 분포가 정규에 가까워진다는 점이다.
- 이 결과 때문에 표본평균을 기준으로 한 z-test, t-test, 평균의 신뢰구간 같은 절차를 정규분포 또는 t분포 근사로 정당화할 수 있다.
- 따라서 중심극한정리는 가설검정의 계산 공식만 뒷받침하는 것이 아니라, 왜 그런 검정이 가능한지 설명하는 이론적 배경이다.


## 5. 신뢰구간, 오차범위, 표본수 결정

- 비율과 평균의 신뢰구간, margin of error, 필요한 sample size 계산은 거의 독립된 출제 축으로 반복된다.
- 문항은 보통 `주어진 표본으로 95% 신뢰구간을 구하라`, `오차범위를 일정 수준 이하로 줄이려면 표본이 얼마나 필요하냐`의 두 단계로 구성된다.
- 좋은 출제는 계산만으로 끝내지 않고, 구간이 무엇을 의미하는지, 신뢰수준을 높이면 왜 구간이 넓어지는지, 표본 수가 왜 오차범위를 줄이는지 문장으로 해석하게 만든다.
- 학생들은 종종 신뢰구간 안에 모수가 들어갈 확률을 잘못 해석하거나, margin of error와 표준오차를 혼동한다. 이 오개념을 드러내는 문장을 붙이는 것이 좋다.
- 표본수 문항은 반올림 처리, 보수적 추정, 두 비율 비교와 단일 비율 추정을 구분하는지까지 확인할 수 있어 채점 변별력이 높다.
- 실제 출제에서는 `CI 계산`과 `해석`을 반드시 함께 묶는 편이 좋다. 식만 맞추고 의미를 틀리는 학생과, 의미는 알지만 수치 계산이 약한 학생을 구분할 수 있기 때문이다.
- 오차범위 문항은 학생이 $z^* \times SE$ 구조를 이해하는지 확인하는 데 좋다. 신뢰수준을 높이거나 표본수를 늘릴 때 무엇이 어떻게 변하는지를 설명형으로 붙이면 더 효과적이다.
- 비율 차이 신뢰구간과 단일 비율 신뢰구간은 표준오차 공식과 해석 대상이 다르므로, 이를 구분해서 묻게 해야 한다.
- 채점에서는 `추정량`, `표준오차`, `임계값`, `오차범위`, `구간 해석`, `필요 표본수 반올림`을 분리해서 보는 것이 적절하다.
- 단일 비율 문항에서는 $\hat p$와 SE를 따로 쓰게 하는 것이 좋다. 학생이 공식만 대입하고 각 요소의 의미를 설명하지 못하는 경우가 많기 때문이다.
- 필요 표본수 문항은 계산 뒤 반드시 올림 처리하게 해야 한다. 목표 오차범위를 넘지 않으려면 내림이 아니라 올림이라는 점을 분명히 해야 한다.
- 두 비율 비교 문항은 가장 난도가 높으므로, `비율 차이의 방향`, `0 포함 여부`, `가설검정과 신뢰구간 결론의 일치`까지 해석하게 해야 한다.

### 실제 문항

---


#### 문항 1

If a higher confidence level means that we are more confident about the number we are reporting, why don't we always report a confidence interval with the highest possible confidence level? (10 점)

---

#### 해설

- 신뢰구간은 `신뢰수준`과 `정밀도` 사이의 교환관계를 가진다.
- 예를 들어 95% 신뢰구간보다 99% 신뢰구간이 더 많은 반복표집에서 모수를 포함하도록 만들려면, 임계값 $z^*$가 더 커져야 한다. 그러면 오차범위
  $$ME=z^*\times SE$$
  가 커지고 구간은 더 넓어진다.
- 구간이 너무 넓으면 실제 의사결정에 도움이 되지 않을 수 있다. 따라서 항상 가장 높은 신뢰수준을 쓰는 것이 아니라, `충분한 신뢰성`과 `충분한 정밀성` 사이에서 적절한 수준을 고르는 것이 맞다.

---


#### 문항 2

B 라는 정치인이 있는데 그사람의 지지도를 조사하였다. 랜덤샘플한 100 명중 B 를 지지하는 사람이 40 명 이였다. B 를 지지도의 오차범위를 95% 의 신뢰도로 구하시오.

---

#### 해설

- 표본비율은
  $$\hat p=\frac{40}{100}=0.40$$
- 표준오차는
  $$
  SE=\sqrt{\frac{\hat p(1-\hat p)}{n}}
  =\sqrt{\frac{0.4\cdot 0.6}{100}}
  =\sqrt{0.0024}\approx 0.0490
  $$
- 95% 오차범위는
  $$
  ME=1.96\times 0.0490\approx 0.0960
  $$
- 따라서 95% 신뢰구간은
  $$
  0.40\pm 0.0960=(0.304,\,0.496)
  $$
- 즉 모집단 지지율은 약 `30.4%`에서 `49.6%` 사이로 추정된다.

---


#### 문항 3

[5 점] 다음 관찰값을 바탕으로 샘플에 대한 모집단 평균의 신뢰구간을 구하세요. (이때 6 번의 t 분포표를 참고하세요)

- Sample 평균 = 20
- Sample 표준편차 = 4
- Sample 의 수 = 10

신뢰구간 = [ ???, ??? ]

---

#### 해설

- 표본평균 $\bar x=20$, 표본표준편차 $s=4$, 표본크기 $n=10$ 이다.
- 모집단 표준편차를 모르므로 t 분포를 사용하고, 자유도는
  $$df=n-1=9$$
- 95% 신뢰구간에서 $t^* \approx 2.262$ 이다.
- 표준오차는
  $$
  SE=\frac{s}{\sqrt{n}}=\frac{4}{\sqrt{10}}\approx 1.2649
  $$
- 오차한계는
  $$
  ME=t^*SE=2.262\times 1.2649\approx 2.8612
  $$
- 따라서 신뢰구간은
  $$
  20\pm 2.8612=(17.1388,\,22.8612)
  $$
- 즉 답은 `약 [17.14, 22.86]`이다.

---


#### 문항 4

We are interested in estimating the proportion of students at a university who smoke. Out of a random sample of 100 students from the university, 20 students smoke (10 점)

1. Calculate a 95% confidence interval for the proportion of students at the university who smoke.
2. If we wanted the margin of error to be no larger than 2% at a 95% confidence level for the proportion of students who smoke, how big of a sample would we need?

---

#### 해설

- 1) 표본비율은
  $$\hat p=\frac{20}{100}=0.20$$
- 표준오차는
  $$
  SE=\sqrt{\frac{0.2(0.8)}{100}}=0.04
  $$
- 95% 오차범위는
  $$
  1.96\times 0.04=0.0784
  $$
- 따라서 95% 신뢰구간은
  $$
  0.20\pm 0.0784=(0.1216,\,0.2784)
  $$
- 2) 목표 오차범위가 0.02일 때 필요한 표본수는
  $$
  n=\frac{z^{*2}\hat p(1-\hat p)}{ME^2}
  =\frac{1.96^2\cdot 0.2\cdot 0.8}{0.02^2}
  $$
  $$
  =\frac{3.8416\cdot 0.16}{0.0004}=1536.64
  $$
- 표본수는 올림해야 하므로 `1537명`이 필요하다.

---


#### 문항 5

We are interested in estimating the proportion of students at a university who smoke. Out of a random sample of 100 students from the university, 20 students smoke (10 점)

1. Calculate a 95% confidence interval for the proportion of students at the university who smoke.
2. If we wanted the margin of error to be no larger than 3% at a 95% confidence level for the proportion of students who smoke, how big of a sample would we need?

---

#### 해설

- 신뢰구간 계산은 문항 4와 동일하다.
  $$
  \hat p=0.20,\quad SE=0.04,\quad 95\%\ CI=(0.1216,\,0.2784)
  $$
- 목표 오차범위가 0.03이면
  $$
  n=\frac{1.96^2\cdot 0.2\cdot 0.8}{0.03^2}
  =\frac{3.8416\cdot 0.16}{0.0009}
  \approx 682.95
  $$
- 올림하면 필요한 표본수는 `683명`이다.

---


#### 문항 6

We are interested in estimating the proportion of students at a university who smoke. Out of a random sample of 100 students from the university, 10 students smoke (5 점)

1. Calculate a 95% confidence interval for the proportion of students at the university who smoke.
2. If we wanted the margin of error to be no larger than 1% at a 95% confidence level for the proportion of students who smoke, how big of a sample would we need? (cf. `pnorm(1.96) = 0.975` in R)

---

#### 해설

- 표본비율은
  $$\hat p=\frac{10}{100}=0.10$$
- 표준오차는
  $$
  SE=\sqrt{\frac{0.1\cdot 0.9}{100}}=\sqrt{0.0009}=0.03
  $$
- 95% 오차범위는
  $$
  1.96\times 0.03=0.0588
  $$
- 따라서 신뢰구간은
  $$
  0.10\pm 0.0588=(0.0412,\,0.1588)
  $$
- 목표 오차범위가 0.01이면
  $$
  n=\frac{1.96^2\cdot 0.1\cdot 0.9}{0.01^2}
  =\frac{3.8416\cdot 0.09}{0.0001}=3457.44
  $$
- 올림하면 `3458명`이 필요하다.

---


#### 문항 7

As part of a quality control process for computer chips, an engineer at a factory randomly samples 200 chips during a week of production to test the current rate of chips with severe defects. She finds that 20 of the chips are defective. (각 1 점, 총 6 점)

(a) What population is under consideration in the data set?

(b) What parameter is being estimated?

(c) What is the point estimate for the parameter?

(d) What is the name of the statistic can we use to measure the uncertainty of the point estimate?

(e) Compute the value from part (d) for this context.

(f) The historical rate of defects is 5%. Should the engineer be surprised by the observed rate of defects during the current week?

---

#### 해설

- (a) 모집단은 그 주에 생산된 `전체 칩`이다.
- (b) 추정하려는 모수는 심각한 결함 칩의 실제 비율 $p$ 이다.
- (c) 점추정량은
  $$\hat p=\frac{20}{200}=0.10$$
- (d) 이 점추정량의 불확실성을 재는 통계량은 `표준오차(SE)`이다.
- (e) 값은
  $$
  SE=\sqrt{\frac{\hat p(1-\hat p)}{n}}
  =\sqrt{\frac{0.10\cdot 0.90}{200}}
  =\sqrt{0.00045}\approx 0.0212
  $$
- (f) 역사적 결함률이 5%라면, 그 값이 귀무가설이라고 볼 때
  $$
  z=\frac{0.10-0.05}{\sqrt{0.05\cdot 0.95/200}}
  \approx \frac{0.05}{0.0154}\approx 3.24
  $$
  이다. 이는 상당히 큰 값이므로 현재 주의 결함률 10%는 과거 5%와 비교할 때 꽤 이례적이라고 보는 것이 자연스럽다.

---


#### 문항 8

A 2010 survey asked 827 randomly sampled registered voters in California “Do you support? Or do you oppose? Drilling for oil and natural gas off the Coast of California? Or do you not know enough to say?” Below is the distribution of responses, separated based on whether or not the respondent graduated from college. (20 점) 참고: `pnorm(1.96) = 0.9750`

|   | College Grad Yes | College Grad No |
|---|---:|---:|
| Support | 154 | 132 |
| Oppose | 180 | 126 |
| Do not know | 104 | 131 |
| Total | 438 | 389 |

1. Use 95% CI (confidence interval method) to determine if the data provide strong evidence that the proportion of college graduates who do not have an opinion on this issue is different than that of non-college graduates.
2. Use HT (hypothesis test method) to determine if the data provide strong evidence that the proportion of college graduates who support off-shore drilling in California is different than that of non-college graduates.

---

#### 해설

- 1) `Do not know` 비율을 비교하면
  $$
  \hat p_1=\frac{104}{438}\approx 0.2374,\qquad
  \hat p_2=\frac{131}{389}\approx 0.3368
  $$
  따라서 차이는
  $$
  \hat p_1-\hat p_2\approx -0.0994
  $$
- 비율 차이의 표준오차는
  $$
  SE=\sqrt{\frac{0.2374(0.7626)}{438}+\frac{0.3368(0.6632)}{389}}
  \approx 0.0314
  $$
- 95% 신뢰구간은
  $$
  -0.0994\pm 1.96(0.0314)=(-0.1609,\,-0.0377)
  $$
  이다. 0을 포함하지 않으므로 두 집단의 무응답 비율은 유의하게 다르며, 비대졸 집단의 무응답 비율이 더 높다.
- 2) `Support` 비율 비교에서는
  $$
  \hat p_1=\frac{154}{438}\approx 0.3516,\qquad
  \hat p_2=\frac{132}{389}\approx 0.3393
  $$
  pooled proportion은
  $$
  \hat p=\frac{154+132}{438+389}=\frac{286}{827}\approx 0.3458
  $$
- 검정통계량은
  $$
  z=\frac{0.3516-0.3393}{\sqrt{\hat p(1-\hat p)(1/438+1/389)}}\approx 0.37
  $$
  이므로 two-sided p-value는 약 `0.711`이다.
- 따라서 support 비율 차이에 대해서는 강한 증거가 없다고 결론내린다.


## 6. 가설검정, p-value, Type I / Type II error

- 이 섹션은 H0/H1를 올바르게 세우고, reject 또는 fail to reject를 문맥 속 결론으로 번역하는 능력을 평가한다.
- 특히 약효, 치료, 실제 생활 사례를 주고 Type I error와 Type II error를 서술하게 하면 정의 암기가 아니라 의미 이해를 확인할 수 있다.
- 좋은 문항은 p-value를 단순히 수치로 말하게 하지 않고, 그 값이 현재 자료와 귀무가설의 관계를 어떻게 말해 주는지를 설명하게 해야 한다.
- 학생들이 가장 자주 틀리는 지점은 `귀무가설이 참일 확률`과 `관측자료가 귀무가설 아래에서 얼마나 드문가`를 혼동하는 것이다. 이 차이를 드러내는 문장형 채점이 필요하다.
- 또한 신뢰구간과 가설검정이 왜 같은 결론을 주는지 연결시키면 이 영역과 추론 영역을 함께 점검할 수 있다.
- 출제는 가능하면 실제 문맥 속 주장과 연결되어야 한다. `효과가 있는가`, `더 선호한다고 말할 수 있는가` 같은 서술을 귀무가설과 대립가설의 문장으로 다시 쓰게 하면 이해 수준 차이가 분명히 드러난다.
- Type I, II error는 기호 정의보다 사례 번역이 핵심이다. 약이 실제로 효과 없는데 있다고 판단한 경우와, 실제로 효과 있는데 없다고 판단한 경우를 문장으로 분리해 쓰게 해야 한다.
- p-value 문항은 단순히 작다/크다보다 `그래서 귀무가설을 기각하는가`, `그 결론을 현실 문장으로 어떻게 바꾸는가`까지 요구해야 한다.
- 채점 기준은 `가설 설정`, `검정 방향`, `통계량 또는 판단 논리`, `결론의 문맥 번역`, `오류 해석`으로 세분하는 것이 좋다.

### 실제 문항

---


#### 문항 1

어떤 환자가 정신질환을 겪고 있다. 이 환자를 위하여 의사가 항우울제를 처방하였다. 그러나 이 환자는 이 약을 꾸준하게 복용함에도 이약의 효능에 대하여 의심스러워 했다. 그러나 두 달 후 이 환자는 자신의 증상이 개선되었음을 느끼게 되었고 약이 효능이 있다는 것을 결국 인정하게 되었다. (5 점)

(a) 이 때 이 환자가 초기에 항우울제의 효능에 대해서 의심하였을 때 이에 관한 가설검정을 수행한다면 사용할 수 있는 가정을 쓰시오 ($H_0$과 $H_A$ 각각)

(b) 이 경우 Type 1 Error 는 무엇인가?

(c) 이 경우 Type 2 Error 는 무엇인가?

---

#### 해설

- 귀무가설 $H_0$ 는 `항우울제는 효과가 없다`로 두고, 대립가설 $H_A$ 는 `항우울제는 효과가 있다`로 두는 것이 자연스럽다.
- Type I error 는 실제로 약효가 없는데도 자료를 보고 약이 효과가 있다고 잘못 결론내리는 경우다. 즉, 거짓 양성에 해당한다.
- 반대로 Type II error 는 실제로 약효가 있는데도 검정 결과 효과가 없다고 결론내리는 경우다. 즉, 거짓 음성이다.
- 이 문항의 핵심은 기호 정의 자체보다, 오류를 실제 의료 문맥의 문장으로 정확히 번역할 수 있는지에 있다.

---


#### 문항 2

현재 이 과목은 24명의 수강생이 있다. 이중 8명이 홀수학번이고 16명이 짝수학번이다. 이 과목을 짝수학번들이 더 선호한다고 할 수 있는가? 통계적으로 분석하시오. 다만 각 조건에 해당하는 인원이 10명이하이나 이를 무시하고 분석하시오. (5점)

---

#### 해설

- 짝수 학번 학생이 이 과목을 더 선호하는지 보려면, 귀무가설은 `짝수 학번과 홀수 학번의 선호 비율이 같다`, 즉 $H_0:p=0.5$로 둘 수 있다.
- 대립가설은 `짝수 학번 비율이 더 크다`, 즉 $H_A:p>0.5$ 이다. 표본에서는 짝수 학번이 24명 중 16명이므로 $\hat p=16/24=0.6667$ 이다.
- 이를 기준으로 검정통계량을 계산하면 $z \approx 1.633$ 이고, one-sided p-value는 약 `0.051`이 나온다.
- 따라서 5% 유의수준에서는 귀무가설을 기각하기 어렵다. 즉, 표본상 짝수 학번이 더 많아 보이기는 하지만 이를 통계적으로 `유의하게 더 선호한다`고 단정하기에는 근거가 약하다고 결론내리는 것이 맞다.


## 7. t-test와 paired t-test

- 이 개념의 핵심은 `두 집단 비교` 자체보다 `무엇이 독립 표본이고 무엇이 대응 표본인가`를 구분하는 데 있다.
- 출제는 pooled variance, 표준오차, 자유도, t 통계량, rough p-value 계산을 요구하면서도, 왜 paired가 더 적절한지 또는 왜 결과가 달라지는지를 설명하게 해야 한다.
- 같은 숫자 자료에 대해 two-sample t-test와 paired t-test를 모두 적용시키는 문항은 매우 좋은 설계다. 대응 구조를 이해하지 못하면 식 선택부터 무너진다.
- 학생들은 종종 두 방법을 공식 차이로만 외운다. 따라서 문항에는 `같은 피험자 반복 측정인지`, `짝이 맞는 관측인지`, `independence가 어디에 필요한지`를 분명히 드러내야 한다.
- 채점에서는 가설 설정, 평균차 정의, df, 표준오차, t 값, 기각 여부, 그리고 선택한 검정의 정당화까지 단계별로 보는 것이 좋다.
- 좋은 문항은 동일한 원자료를 두 가지 방식으로 분석하게 하여, 대응 구조를 반영했을 때 왜 표준오차가 줄거나 결론이 달라질 수 있는지를 보여준다.
- 학생들이 자주 틀리는 지점은 paired t-test에서 원자료 두 집단이 아니라 `차이값 하나의 표본`을 분석한다는 사실이다. 따라서 차이의 평균과 차이의 분산을 따로 쓰게 하는 구성이 중요하다.
- p-value table을 주고 rough comparison만 하게 하는 방식은 계산기 의존 없이 자유도와 임계값 해석을 점검하기에 좋다.
- 채점은 `적절한 검정 선택`, `차이 정의`, `표준오차 계산`, `자유도`, `결론`, `왜 두 결과가 다른가에 대한 설명`까지 봐야 한다.

### 실제 문항

---


#### 문항 1

다음 A, B 두 그룹의 데이터를 이용하여 두가지 방법으로 t-test 를 시행하고자 한다. 빈칸을 채우시오 (20 점)

##### 데이터

| | A | B | Total |
|---|---|---|---|
| Value | 0, 0, 2, 2 | 1, 1, 2, 4 | |
| N | 4 | 4 | 8 |
| $\sum X$ | 4 | 8 | 12 |
| $\sum X^2$ | 8 | 22 | 30 |
| SS | 4 | 6 | 12 |
| Mean | 1 | 2 | 1.5 |

##### (1) Two sample t-test (11 점)

- $H_0$ (two tailed) & $H_A$ (two tailed): ?
- Sample mean(A) – Sample mean(B) = ?
- Degree of Freedom = ?
- Pooled variance of A and B = ?
- Estimated variance (sample mean of A – sample mean of B) for t-test = ?
- $t(?) = ?$
- $p = ?$ (아래의 p-value 테이블을 보고 rough 한 근사치를 넣으세요)
- Reject with 10% significance level?

##### (2) Paired t-test (9 점)

- $H_0$ (two tailed) & $H_A$ (two tailed): ?
- Sample mean(A) – Sample mean(B) = ?
- Degree of Freedom = ?
- Estimated variance (sample mean of difference) for t-test = ?
- $t(?) = ?$
- $p = ?$ (아래의 p-value 테이블을 보고 rough 한 근사치를 넣으세요)
- Reject with 10% significance level?

##### p-value Table

| Two tails | 0.100 | 0.050 | 0.010 |
|---|---|---|---|
| df 3 | 2.35 | 3.18 | 5.84 |
| df 4 | 2.13 | 2.78 | 4.60 |
| df 5 | 2.02 | 2.57 | 4.03 |
| df 6 | 1.94 | 2.45 | 3.71 |
| df 7 | 1.89 | 2.36 | 3.50 |
| df 8 | 1.86 | 2.31 | 3.36 |
| df 9 | 1.83 | 2.26 | 3.25 |
| df 10 | 1.81 | 2.23 | 3.17 |

---

#### 해설

- (1) Two-sample t-test
- 귀무가설과 대립가설은
  $$H_0:\mu_A-\mu_B=0,\qquad H_A:\mu_A-\mu_B\ne 0$$
- 표본평균 차이는
  $$\bar X_A-\bar X_B=1-2=-1$$
- 자유도는
  $$df=n_A+n_B-2=4+4-2=6$$
- pooled variance는
  $$
  s_p^2=\frac{SS_A+SS_B}{df}=\frac{4+6}{6}=\frac{10}{6}=1.6667
  $$
- 평균차의 분산과 표준오차는
  $$
  Var(\bar X_A-\bar X_B)=s_p^2\left(\frac14+\frac14\right)=1.6667\times 0.5=0.8333
  $$
  $$
  SE=\sqrt{0.8333}\approx 0.9129
  $$
- 검정통계량은
  $$
  t(6)=\frac{-1-0}{0.9129}\approx -1.095
  $$
- 절댓값이 df=6의 10% 양측 기준값 1.94보다도 작으므로 p-value는 `0.10보다 크다`. 따라서 10% 유의수준에서도 기각하지 못한다.
- (2) Paired t-test
- 차이값을 $D=A-B$라 두면 자료는 `-1, -1, 0, -2` 이다.
- 차이의 평균은
  $$\bar D=\frac{-1-1+0-2}{4}=-1$$
- 자유도는
  $$df=4-1=3$$
- 차이의 제곱합은
  $$
  SS_D=\sum (D_i-\bar D)^2=0^2+0^2+1^2+(-1)^2=2
  $$
- 차이의 표본분산은
  $$
  s_D^2=\frac{SS_D}{3}=\frac23=0.6667
  $$
  평균차의 분산과 표준오차는
  $$
  Var(\bar D)=\frac{s_D^2}{4}=0.1667,\qquad SE=\sqrt{0.1667}\approx 0.4082
  $$
- 따라서
  $$
  t(3)=\frac{-1-0}{0.4082}\approx -2.449
  $$
- df=3에서 10% 양측 임계값은 2.35, 5% 양측 임계값은 3.18이므로 p-value는 `0.10과 0.05 사이`이다. 따라서 10%에서는 기각, 5%에서는 기각하지 못한다.
- 두 검정 결과가 다른 이유는 paired t-test가 짝지어진 구조를 반영해 개인차를 제거하므로 표준오차가 더 작아졌기 때문이다.

---


#### 문항 2

[15 점] 다음 A, B 두 그룹의 데이터를 이용하여 두가지 방법으로 t-test 분석을 하고자 한다. 빈칸을 채우세요

|   | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| A | -1 | -1 | 0 | 2 |
| B | 1 | 1 | 3 | 3 |
| Diff | 2 | 2 | 3 | 1 |

|   | A | B | Total |
|---|---:|---:|---:|
| N | 4 | 4 | 8 |
| $\Sigma X$ | 0 | 8 | 8 |
| $\Sigma X^2$ | 6 | 20 | 26 |
| SS | 6 | 4 | 18 |
| Mean | 0 | 2 | 1 |

1. Two sample t-test  
H0 (two tailed): ?  
Mean(A) - Mean(B) = ?  
Degree of Freedom = ?  
Pooled variance of A and B = ?  
Estimated S.E. (standard error) for t-test = ?  
t(?) = (??? - ???) / Above estimated S.E. = ?  
p = ? (아래의 p-value 테이블을 보고 rough 한 근사치를 넣으세요)  
Reject or fail to reject? (5% significance level)

2. Paired t-test  
H0 (two tailed): ?  
Degree of Freedom = ?  
Estimated variance for t-test = ?  
t(?) = (??? - ???) / Estimated Error = ???  
p = ? (아래의 p-value 테이블을 보고 rough 한 근사치를 넣으세요)  
Reject or fail to reject ? (5% significance level)

| Two tails | 0.100 | 0.050 | 0.010 |
|---|---:|---:|---:|
| One tail | 0.050 | 0.025 | 0.005 |
| df 3 | 2.35 | 3.18 | 5.84 |
| df 4 | 2.13 | 2.78 | 4.60 |
| df 5 | 2.02 | 2.57 | 4.03 |
| df 6 | 1.94 | 2.45 | 3.71 |
| df 7 | 1.89 | 2.36 | 3.50 |
| df 8 | 1.86 | 2.31 | 3.36 |
| df 9 | 1.83 | 2.26 | 3.25 |
| df 10 | 1.81 | 2.23 | 3.17 |

---

#### 해설

- 1) Two-sample t-test
- 가설은
  $$H_0:\mu_A-\mu_B=0,\qquad H_A:\mu_A-\mu_B\ne 0$$
- 평균차는
  $$\bar X_A-\bar X_B=0-2=-2$$
- 자유도는
  $$df=4+4-2=6$$
- pooled variance는
  $$
  s_p^2=\frac{SS_A+SS_B}{6}=\frac{6+4}{6}=1.6667
  $$
- 평균차의 표준오차는
  $$
  SE=\sqrt{1.6667\left(\frac14+\frac14\right)}=\sqrt{0.8333}\approx 0.9129
  $$
- 따라서
  $$
  t(6)=\frac{-2-0}{0.9129}\approx -2.191
  $$
- df=6에서 5% 양측 기준값은 2.45이므로 절댓값 2.191은 여기에 못 미친다. p-value는 `0.10과 0.05 사이`이므로 5%에서 기각하지 못한다.
- 2) Paired t-test
- 차이값은 `-2, -2, -3, -1` 이고 평균은
  $$\bar D=\frac{-8}{4}=-2$$
- 자유도는 `3`.
- 차이 제곱합은
  $$
  SS_D=(0)^2+(0)^2+(-1)^2+(1)^2=2
  $$
  따라서
  $$
  s_D^2=\frac{2}{3}=0.6667,\qquad Var(\bar D)=\frac{0.6667}{4}=0.1667
  $$
  $$
  SE=\sqrt{0.1667}\approx 0.4082
  $$
- 검정통계량은
  $$
  t(3)=\frac{-2-0}{0.4082}\approx -4.899
  $$
- df=3에서 5% 양측 기준값은 3.18이므로 귀무가설을 기각한다. p-value는 `0.05보다 작고 0.01보다 크다`.
- 같은 자료인데 paired 분석에서 더 강한 결과가 나오는 이유는 각 쌍 내 차이의 변동이 작아서 표준오차가 크게 줄어들기 때문이다.

---


#### 문항 3

다음과 같은 두 그룹 A, B 에 대해서 two sample t-test 와 Mann Whitney U test 를 1% 의 유의도로 각각 실시하시오. 두 test 가 차이가 있는가? 있으면 왜 차이가 생기는지 설명하시오. (15 점)

**참고:** $pnorm(2.58) = 0.9950$

**U 를 구한 후 p 를 계산할 때 다음 수식을 활용하여 Z 로 근사**

| | A | B |
|---|---|---|
| Data | 1, 2, 3, 7 | 6, 10, 12, 14 |
| $\sum X$ | 13 | 42 |
| $\sum X^2$ | 63 | 476 |

---

#### 해설

- 먼저 two-sample t-test를 계산하면
  $$
  \bar X_A=\frac{13}{4}=3.25,\qquad \bar X_B=\frac{42}{4}=10.5
  $$
  $$
  SS_A=63-\frac{13^2}{4}=20.75,\qquad SS_B=476-\frac{42^2}{4}=35
  $$
  $$
  s_p^2=\frac{20.75+35}{6}=9.2917
  $$
  $$
  SE=\sqrt{9.2917\left(\frac14+\frac14\right)}=\sqrt{4.6458}\approx 2.1554
  $$
  $$
  t(6)=\frac{3.25-10.5}{2.1554}\approx -3.363
  $$
- df=6에서 1% 양측 기준값은 3.71이므로 절댓값 3.363은 여기에 못 미친다. 따라서 1% 유의수준에서는 기각하지 못한다.
- Mann-Whitney U test에서는 합친 자료의 순위가 `1,2,3,5,4,6,7,8`이 아니라 값 크기 기준으로 A의 순위합이
  $$R_A=1+2+3+5=11$$
  이다. 따라서
  $$
  U_A=R_A-\frac{n_A(n_A+1)}{2}=11-10=1
  $$
- 정규근사하면
  $$
  z=\frac{U-\frac{n_1n_2}{2}}{\sqrt{\frac{n_1n_2(n_1+n_2+1)}{12}}}
  =\frac{1-8}{\sqrt{12}}\approx -2.021
  $$
- 1% 양측 기준은 약 `2.58`이므로 이것도 기각하지 못한다.
- 두 검정 모두 1%에서는 비유의이지만, t-test는 평균 차이를 직접 보고 Mann-Whitney는 순위 차이를 본다. 자료가 서열척도이거나 정규성 가정이 약할 때는 Mann-Whitney가 더 적절할 수 있다.


## 8. 비모수 검정

- 비모수 검정은 단순히 `정규분포가 아니면 쓰는 방법`으로 다루면 얕다. 실제 기출은 Mann-Whitney, Wilcoxon, Friedman, Kruskal-Wallis를 서로 다른 설계와 자료형에 맞게 고르게 한다.
- Likert scale, small n, 순위 기반 비교, 이상치에 민감한 자료를 제시하고 왜 t-test나 ANOVA 대신 비모수 검정을 써야 하는지 설명하게 하는 구성이 적합하다.
- 좋은 문항은 비모수 검정을 적용한 뒤, 대응되는 모수검정과 무엇이 같고 무엇이 다른지까지 연결한다. 예를 들어 rank를 쓰는 이유, median 중심 해석, 가정 완화의 의미를 묻게 된다.
- 학생들이 자주 하는 오해는 `비모수는 항상 더 약하다`, `항상 p가 더 크다`, `순위를 쓰면 부정확하다` 같은 식의 단정이다. 참/거짓형이나 비교형으로 이런 오개념을 바로 드러낼 수 있다.
- 계산형 문항에서는 순위 부여, U 통계량, 정규근사, 근사 p-value 판정까지 보게 하면 충분한 변별력이 생긴다.
- 출제에서는 자료형과 설계를 읽어내는 능력이 중요하다. 독립집단인지 대응집단인지, 서열척도인지 연속형인지에 따라 어떤 비모수 검정을 써야 하는지가 달라진다.
- Mann-Whitney 문항은 원자료 값보다 순위합이 핵심이라는 점을 학생이 이해하는지 보게 해야 한다. 단순 계산보다 왜 순위를 쓰는지까지 설명하게 하면 더 좋다.
- 작은 표본에서도 근사식을 사용하게 하는 문항은 계산력뿐 아니라 근사 해석을 점검하는 장점이 있다. 다만 근사 사용을 명시하지 않으면 불필요한 혼란을 줄 수 있으므로 조건을 분명히 적는 편이 좋다.
- 채점은 `검정 선택`, `순위 부여`, `통계량`, `근사 판단`, `결론의 문맥 번역`으로 나누는 것이 적절하다.

### 실제 문항

---


#### 문항 1

다음과 같은 두 그룹 A, B 에 대해서 Mann Whitney U test 를 1%의 유의도로 실시하시오. (5 점) 참고: `pnorm(2.58) = 0.9950` in R

- A: 1, 2, 3, 7
- B: 6, 10, 12, 14
- A: $\sum X = 13$, $\sum X^2 = 63$
- B: $\sum X = 42$, $\sum X^2 = 476$

U 를 구한 후 p 를 계산할 때 다음 수식을 활용하여 Z 로 근사

$$
\frac{U_s - \frac{n_1 n_2}{2}}{\sqrt{\frac{n_1 n_2 (n_1 + n_2 + 1)}{12}}}
$$

---

#### 해설

- 자료를 합쳐 크기순으로 정렬하면 `1, 2, 3, 6, 7, 10, 12, 14` 이다.
- A의 값 `1,2,3,7`의 순위는 `1,2,3,5` 이므로
  $$R_A=1+2+3+5=11$$
- 따라서
  $$
  U_A=R_A-\frac{n_A(n_A+1)}{2}=11-\frac{4\cdot 5}{2}=1
  $$
  대칭적으로 $U_B=16-1=15$ 이고, 더 작은 값을 써서 $U=1$로 둔다.
- 정규근사는
  $$
  z=\frac{1-\frac{4\cdot4}{2}}{\sqrt{\frac{4\cdot4\cdot(4+4+1)}{12}}}
  =\frac{1-8}{\sqrt{12}}
  \approx -2.021
  $$
- 1% 양측 유의수준 기준값은 약 `2.58`이므로 $|z|=2.021<2.58$ 이다. 따라서 귀무가설을 기각하지 못한다.
- 즉 순위 기준으로 A와 B가 다르다고 말할 증거는 1% 수준에서는 충분하지 않다.

---


#### 문항 2

다음과 같은 두 그룹 A, B 에 대해서 Mann Whitney U test 를 5%의 유의도로 실시하세요. n 이 매우 작으나 아래 수식으로 근사하여 풀면 된다고 가정하시오. (10 점) 참고: `pnorm(1.96) = 0.975` in R

- A: 2, 2, 4, 7
- B: 5, 9, 10, 12

$$
\frac{U_s - \frac{n_1 n_2}{2}}{\sqrt{\frac{n_1 n_2 (n_1 + n_2 + 1)}{12}}}
$$

U 를 구한 후 p 를 계산할 때 다음 수식을 활용하여 Z 로 근사

---

#### 해설

- 합친 자료를 정렬하면 `2, 2, 4, 5, 7, 9, 10, 12` 이다.
- 값 2가 두 번 반복되므로 두 관측치의 순위는 평균순위 `1.5, 1.5`를 준다.
- A의 순위는 `1.5, 1.5, 3, 5` 이므로
  $$R_A=11$$
- 따라서
  $$
  U_A=R_A-\frac{4\cdot5}{2}=11-10=1
  $$
- 정규근사 통계량은
  $$
  z=\frac{1-8}{\sqrt{12}}\approx -2.021
  $$
- two-sided p-value는 약 `0.043` 이다.
- 5% 유의수준에서는 $|z|>1.96$ 이므로 귀무가설을 기각한다. 즉 두 집단의 위치는 유의하게 다르다고 볼 수 있다.

---


#### 문항 3

[10 점] 다음과 같이 5-point Likert scale(1 점 - 5 점)로 얻은 두 그룹 A, B 에 대해서 Mann Whitney U test 를 5%의 유의도로 실시하시오. A 그룹과 B 그룹은 유의한 차이가 있는가? 참고: `pnorm(1.96) = 0.9750` in R, `nA = 4`, `nB = 5`

- A: 1, 2, 2, 4
- B: 3, 5, 5, 5, 5

U 를 구한 후 p 를 계산할 때 다음 수식을 활용하여 Z 로 근사

H0 (two tailed): ?  
통계량 U = ??  
Z = ??  
Z 는 1.96 보다 (크다, 작다)  
위의 통계량에 따라 p 는 0.05 보다 (크다, 작다)  
Reject or fail to reject ? (5% significance level)

---

#### 해설

- 귀무가설은
  $$H_0:\text{두 집단의 분포 위치가 같다}$$
  이고, 대립가설은 two-tailed 이다.
- 합친 자료 `1,2,2,3,4,5,5,5,5`의 순위를 주면
  - A=`1,2,2,4` 의 순위는 `1, 2.5, 2.5, 5`
  - B=`3,5,5,5,5` 의 순위는 `4, 7.5, 7.5, 7.5, 7.5`
- 따라서
  $$R_A=1+2.5+2.5+5=11$$
  이고
  $$
  U_A=R_A-\frac{4\cdot5}{2}=11-10=1
  $$
- 정규근사는
  $$
  z=\frac{1-\frac{4\cdot5}{2}}{\sqrt{\frac{4\cdot5\cdot(4+5+1)}{12}}}
  =\frac{1-10}{\sqrt{200/12}}
  \approx \frac{-9}{4.0825}\approx -2.205
  $$
- $|z|=2.205>1.96$ 이므로 p-value는 `0.05보다 작다`. 따라서 5% 수준에서 귀무가설을 기각한다.
- 즉 Likert 척도 자료를 순위로 비교했을 때 A와 B 사이에는 유의한 차이가 있다고 결론내린다.


## 9. ANOVA 기본 구조와 가정

- 이 영역은 one-way 또는 two-way ANOVA의 뼈대를 이해하는지 묻는 축이다. SS, df, MS, F를 계산하는 것 자체보다, between-group variability와 within-group variability가 무엇을 뜻하는지 이해하는지가 핵심이다.
- 단일 요인과 두 요인 설계를 구분시키고, effect size, multiple comparison, 가정 위배 가능성 등을 같이 묻는 문항이 자주 나온다.
- 좋은 문제는 표의 빈칸을 채우는 계산에 그치지 않고, `유의한 F가 정확히 무엇을 말하는가`, `왜 사후분석이 필요할 수 있는가`까지 서술하게 해야 한다.
- 학생들이 흔히 ANOVA를 단순히 집단 평균이 다르냐의 yes/no 검정으로만 이해하는데, 실제 출제는 분산 분해의 구조를 알고 있는지 확인하는 방향으로 가는 편이 좋다.
- 가정 문항에서는 독립성, 정규성, 등분산성뿐 아니라 그 가정이 왜 필요한지까지 쓰게 하면 답안 수준 차이가 분명히 난다.
- 출제는 `분산 분해 표 채우기`와 `해석`을 반드시 함께 두는 편이 좋다. 계산은 맞지만 between/within의 의미를 모르는 답안을 걸러낼 수 있기 때문이다.
- Two-way ANOVA에서는 row, column, interaction을 분리해 보게 해야 한다. 특히 interaction을 주효과와 독립된 항으로 이해하는지가 중요하다.
- 사후분석 문항은 ANOVA가 유의하다는 사실만으로 어느 집단이 다른지 알 수 없다는 점을 학생이 정확히 설명하는지 확인하는 데 효과적이다.
- 채점은 `SS 구조 이해`, `자유도`, `F 비율`, `유의성 해석`, `가정 설명`의 다섯 층으로 보는 것이 좋다.

### 실제 문항

---


#### 문항 1

ANOVA 를 수행하기 위해 데이터가 만족해야 하는 성질 세가지에 대해 서술하시오 (5 점)

---

#### 해설

- One-way ANOVA 의 핵심 가정은 세 가지다. 첫째, 각 관측치는 서로 독립이어야 한다. 둘째, 각 집단의 오차 또는 자료가 대체로 정규성을 만족해야 한다. 셋째, 집단 간 분산이 비슷한 등분산성을 가져야 한다.
- 이 세 조건이 크게 무너지면 F 검정의 해석이 왜곡될 수 있다.
- 따라서 정답에서는 가정 이름만 쓰기보다, 각각이 왜 필요한지까지 짧게 설명하는 것이 더 좋은 답안이다.

---


#### 문항 2

다음은 40 명의 참가자가 참여한 실험의 4 (row) X 2 (column) Two-way ANOVA 결과이다. 빈칸에 알맞은 수를 넣으시오. Between subject design 임을 고려하시오. (5 점)

| Source | SS | Df | MS | F |
|---|---|---|---|---|
| Between Group | $SS_{bg} = 50$ |  |  |  |
| Row | $SS_{row} = 20$ |  |  | $F(?, ?) = ?$ |
| Column | $SS_{column} = 10$ |  |  | $F(?, ?) = ?$ |
| Interaction | $SS_{interaction} = ?$ |  |  | $F(?, ?) = ?$ |
| Error | $SS_{error} = ?$ |  |  |  |
| Total | $SS_T = 100$ |  |  |  |

---

#### 해설

- 4×2 between-subject design 이므로
  $$
  df_{row}=4-1=3,\qquad df_{column}=2-1=1,\qquad df_{interaction}=3\times 1=3
  $$
- Between-group 자유도는
  $$df_{bg}=8-1=7$$
  이고, 총 참가자 40명이므로
  $$df_T=40-1=39,\qquad df_{error}=39-7=32$$
- 제곱합은
  $$
  SS_{interaction}=SS_{bg}-SS_{row}-SS_{column}=50-20-10=20
  $$
  $$
  SS_{error}=SS_T-SS_{bg}=100-50=50
  $$
- 평균제곱은
  $$
  MS_{row}=20/3=6.6667,\quad MS_{column}=10/1=10,\quad MS_{interaction}=20/3=6.6667,\quad MS_{error}=50/32=1.5625
  $$
- 따라서
  $$
  F_{row}(3,32)=6.6667/1.5625\approx 4.27
  $$
  $$
  F_{column}(1,32)=10/1.5625=6.40
  $$
  $$
  F_{interaction}(3,32)=6.6667/1.5625\approx 4.27
  $$

---


#### 문항 3

다음 데이타를 가지고 One-way ANOVA 분석을 하시오.

| a | b | c | d |
|---|---|---|---|
| 29 | 22.8 | 21.9 | 23.5 |
| 26.2 | 23.1 | 23.4 | 19.6 |
| 28.8 | 27.7 | 20.1 | 23.7 |
| 33.5 | 27.6 | 27.8 | 20.8 |
| 28.8 | 24 | 19.3 | 23.9 |

---

#### 해설

- 각 집단 평균은
  $$
  \bar a=29.26,\quad \bar b=25.04,\quad \bar c=22.50,\quad \bar d=22.30
  $$
  전체평균은
  $$\bar x=24.775$$
- 집단간 제곱합은
  $$
  SS_{BG}=5\sum (\bar x_j-\bar x)^2
  \approx 157.4335
  $$
- 집단내 제곱합은 각 집단 내부 편차제곱합의 합으로
  $$
  SS_{WG}\approx 112.0840
  $$
- 따라서
  $$
  df_{BG}=4-1=3,\qquad df_{WG}=20-4=16
  $$
  $$
  MS_{BG}=157.4335/3\approx 52.4778
  $$
  $$
  MS_{WG}=112.0840/16\approx 7.0053
  $$
- F 통계량은
  $$
  F(3,16)=\frac{52.4778}{7.0053}\approx 7.49
  $$
- 이 값은 상당히 크므로 네 집단 평균이 모두 같다는 귀무가설은 기각된다. 다만 어느 집단끼리 차이 나는지는 post hoc 분석이 추가로 필요하다.

---


#### 문항 4

다음 반복측정 데이터와 동일한 값들을 독립집단 One-way ANOVA 로 분석한다고 가정하자. 빈칸을 채우시오 (20 점)

| Subject | A | B | C |
|---|---:|---:|---:|
| 1 | 1 | 2 | 3 |
| 2 | 2 | 2 | 3 |
| 3 | 3 | 3 | 4 |
| 4 | 4 | 3 | 4 |
| 5 | 5 | 5 | 6 |

| Source | SS | Df | MS | F | p |
|---|---|---|---|---|---|
| Between Group | $SS_{bg} = ?$ | $df_{bg} = ?$ | $MS_{bg} = ?$ | $F(?, ?) = ?$ | 0.43 |
| Error | $SS_{error} = ?$ | $df_{error} = ?$ | $MS_{error} = ?$ |  |  |
| Total | $SS_T = ?$ | $df_T = 14$ |  |  |  |

3-1. 반복측정 ANOVA 결과(p = 0.0067)와 독립집단 One-way ANOVA 결과(p = 0.43)의 significance 가 다른 이유와 대처방법을 자세하게 설명하시오 (10 점)

---

#### 해설

- 전체 자료의 합은 `50`, 전체평균은
  $$\bar x=\frac{50}{15}=3.\overline{3}$$
- 총제곱합은
  $$
  SS_T=\sum X^2-\frac{(\sum X)^2}{N}=191-\frac{50^2}{15}=25.3333
  $$
- 집단제곱합은 각 조건합이 `15, 15, 20` 이므로
  $$
  SS_{bg}=\frac{15^2}{5}+\frac{15^2}{5}+\frac{20^2}{5}-\frac{50^2}{15}=3.3333
  $$
- 독립집단 ANOVA로 보면
  $$
  SS_{error}=SS_T-SS_{bg}=22.0,\quad df_{bg}=2,\quad df_{error}=12
  $$
  $$
  MS_{bg}=1.6667,\quad MS_{error}=1.8333,\quad F(2,12)=0.9091
  $$
  이므로 p가 커져 유의하지 않다.
- 반면 repeated measure 구조를 반영하면 subject 합이 `6,7,10,11,16` 이므로
  $$
  SS_{subject}=\frac{6^2+7^2+10^2+11^2+16^2}{3}-\frac{50^2}{15}=20.6667
  $$
  $$
  SS_{error}=SS_T-SS_{bg}-SS_{subject}=1.3333
  $$
  $$
  df_{subject}=4,\qquad df_{error}=8
  $$
  $$
  MS_{error}=1.3333/8=0.1667,\qquad F(2,8)=1.6667/0.1667=10.0
  $$
- 즉 반복측정에서는 개인차를 $SS_{subject}$로 따로 분리하므로 error가 크게 줄어든다. 그래서 같은 자료라도 RM ANOVA에서는 유의하고, 독립집단 ANOVA에서는 유의하지 않을 수 있다.


## 10. RM ANOVA, Mixed ANOVA, Interaction, Post Hoc

- 이 섹션은 반복측정 설계와 혼합설계가 일반 ANOVA와 어떻게 다른지 이해하는지를 묻는다. 실제 기출에서 가장 자주 계산형과 해석형이 결합되는 영역 중 하나다.
- 반복측정에서는 subject variation을 따로 떼어내기 때문에 왜 유의성이 달라질 수 있는지, 어떤 error term이 F 분모로 들어가야 하는지, interaction이 무엇을 의미하는지를 설명하게 해야 한다.
- Mixed ANOVA 문항은 A가 between인지 B가 repeated인지 파악하고, 검정해야 할 세 가지 가설, 각 자유도, F 비율을 쓰게 하면 구조 이해를 정확히 평가할 수 있다.
- 좋은 문항은 sphericity, Greenhouse-Geisser correction, post hoc 절차, interaction plot 해석까지 연결해 단순 계산을 넘어 연구설계 해석 능력을 요구한다.
- 채점에서는 SS/df/MS/F 계산, 가설 대응, interaction 해석, 그리고 어떤 비교에 어떤 사후검정을 적용해야 하는지까지 분리해서 보는 것이 적절하다.
- 이 영역은 학생이 가장 많이 헷갈리는 파트라서, 출제 문장 안에 각 요인이 between인지 repeated인지 분명히 박아 두는 것이 좋다. 설계 인식이 틀리면 이후 계산은 전부 무너진다.
- 반복측정과 독립집단을 같은 데이터로 비교시키는 문제는 매우 효과적이다. 왜 RM에서 error term이 줄어들 수 있는지, 왜 p-value가 달라지는지 설명하게 하면 구조 이해가 드러난다.
- interaction 해석 문항은 수치표만 주기보다 plot이나 셀 평균을 함께 주는 편이 좋다. 학생이 `선이 교차한다` 수준을 넘어 어느 조건에서 차이가 커지는지를 말할 수 있어야 한다.
- post hoc 문항은 단순 이름 나열보다 `어떤 상황에서 어떤 비교를 하고 왜 보정이 필요한가`를 쓰게 해야 실제 연구 해석 능력을 볼 수 있다.
- 반복측정 계산형 문항은 총제곱합, 집단제곱합, subject 제곱합, error 제곱합의 관계를 끝까지 연결해 쓰게 해야 한다. 중간 결과만 맞고 구조가 틀린 답을 걸러내려면 각 제곱합의 출처를 설명하게 하는 것이 유효하다.
- mixed ANOVA 문항에서는 `어떤 효과를 어떤 error term으로 나누는가`를 명시적으로 쓰게 해야 한다. A main effect, B main effect, interaction이 서로 다른 분모를 쓸 수 있다는 점이 핵심이다.
- 논문 해석형 문항은 유의성 여부만 말하는 답으로는 부족하다. `어느 수준에서 평균이 더 높거나 낮은가`, `interaction이 유의하지 않다면 그림에서 커 보이는 차이를 어디까지 말할 수 있는가`를 함께 서술하게 해야 한다.

### 실제 문항

---


#### 문항 1

다음과 같은 세가지 그룹에 대해서 RM One-way ANOVA 검정을 실시하였다. 빈칸을 채우시오. (20 점)

| Subject | A | B | C |
|---|---:|---:|---:|
| 1 | 1 | 2 | 3 |
| 2 | 2 | 2 | 3 |
| 3 | 3 | 3 | 4 |
| 4 | 4 | 3 | 4 |
| 5 | 5 | 5 | 6 |

- A: $\Sigma X = 15$, Mean = 3, $\Sigma X^2 = 55$
- B: $\Sigma X = 15$, Mean = 3, $\Sigma X^2 = 51$
- C: $\Sigma X = 20$, Mean = 4, $\Sigma X^2 = 86$

| Source | SS | Df | MS | F | p |
|---|---|---|---|---|---|
| Between Group | $SS_{bg} = ?$ | $df_{bg} = ?$ | $MS_{bg} = ?$ | $F(?, ?) = ?$ | 0.0067 |
| Subject | $SS_{subject} = ?$ | $df_{subj} = ?$ |  |  |  |
| Error | $SS_{error} = ?$ | $df_{error} = ?$ | $MS_{error} = ?$ |  |  |
| Total | $SS_T = ?$ | $df_T = 14$ |  |  |  |

---

#### 해설

- 전체합은 `50`, 전체평균은
  $$\bar x=50/15=3.\overline{3}$$
- 총제곱합은
  $$
  SS_T=\sum X^2-\frac{(\sum X)^2}{N}=192-\frac{2500}{15}=25.3333
  $$
- 집단제곱합은
  $$
  SS_{bg}=\frac{15^2}{5}+\frac{15^2}{5}+\frac{20^2}{5}-\frac{2500}{15}=3.3333
  $$
- subject 합은 `6, 7, 10, 11, 16` 이므로
  $$
  SS_{subject}=\frac{6^2+7^2+10^2+11^2+16^2}{3}-\frac{2500}{15}=20.6667
  $$
- error는
  $$
  SS_{error}=SS_T-SS_{bg}-SS_{subject}=25.3333-3.3333-20.6667=1.3333
  $$
- 자유도는
  $$
  df_{bg}=3-1=2,\quad df_{subject}=5-1=4,\quad df_{error}=(3-1)(5-1)=8
  $$
- 평균제곱은
  $$
  MS_{bg}=3.3333/2=1.6667,\qquad MS_{error}=1.3333/8=0.1667
  $$
- 따라서
  $$
  F(2,8)=\frac{1.6667}{0.1667}=10.0
  $$
- p값은 문항에 제시된 대로 `0.0067` 수준으로 유의하다.

---


#### 문항 2

다음 문제의 빈칸의 숫자를 채워 넣으시오 (15 점)

Are We There Yet?: The Role of Gender on the Effectiveness and Efficiency of User-Robot Communication in Navigational Tasks by Koulouri et al.

**Objective**

Exploring the dialogs between partners of the same and of different gender in a simulated Human-Robot Interaction study

**Between-participants factors**

1. “user” gender (female users versus male users)
2. “robot” gender (female “robots” versus male “robots”).

Measured Variable: time taken for a task in each condition

2X2 Two Way ANOVA

| Source | SS | df | MS | F | Sig. |
|---|---:|---:|---:|---:|---:|
| user | 3908.349 | ??? | 3908.349 | .858 | .363 |
| robot | 41996.727 | ??? | 41996.727 | 9.225 | .006 |
| user * robot | 10734.415 | ??? | 10734.415 | 2.358 | .138 |
| Error | 109264.636 | ??? | 4552.693 |  |  |
| Corrected Total |  | 27 |  |  |  |

- FF: Female User / Female Robot
- FM: Female User / Male Robot
- MF: Male User / Female Robot
- MM: Male User / Male Robot

[image: bar chart of average completion time per task for FF, FM, MF, and MM pairs; FM is the lowest, FF and MF are higher, MM is intermediate]

The results associated with the average time taken to complete each task suggest that pair configuration has a significant impact on the speed with which the pairs completed each task, F(3,24) = 4.038, p = 0.019. The post-hoc test indicates that statistically-reliable differences are found between the FM and FF pairs (p = 0.05) and between the FM and MF pairs (p = 0.05). In particular, FM pairs were significantly quicker (306 seconds) by almost two minutes than FF and MF pairs (425 seconds and 409 seconds, respectively). Figure 4 shows the average completion time per task for the four pair configurations.

The two-way analysis of variance revealed a main effect of ‘robot’ gender

$(F(????, ????) = ?????, p = ?????)$, which indicated that the mean time per task was significantly $(lower????/higher????)$ for male ‘robots’ than female ‘robots’. The main effect of user gender $(p=????)$ and the user gender X ‘robot’ gender interaction $(p=????)$ were not found to be significant. This suggests that only ‘$(user????/robot????)$’ gender was related to completion time.

---

#### 해설

- 2×2 between-subject ANOVA 이므로 각 주효과와 interaction의 자유도는 모두 `1`이다.
- corrected total df가 `27`이므로 전체 표본수는 `28`이고, error 자유도는
  $$27-(1+1+1)=24$$
  이다.
- 따라서 빈칸은 다음과 같이 채워진다.
  - user: `df=1`
  - robot: `df=1`
  - user*robot: `df=1`
  - error: `df=24`
- 본문에 들어갈 결과는
  $$F(1,24)=9.225,\ p=.006$$
  이고, 이는 robot gender의 주효과가 유의하다는 뜻이다.
- Figure 4를 보면 네 셀 평균은 대략 `FF=425`, `FM=306`, `MF=409`, `MM`은 중간 수준이다. 특히 male robot 조건(FM, MM)이 female robot 조건(FF, MF)보다 전반적으로 completion time이 짧다.
- 따라서 mean time per task는 male robots에서 더 `lower`했고, user gender의 p값은 `.363`, interaction의 p값은 `.138`이다. 결론적으로 completion time과 관련된 것은 `robot` gender라고 해석한다.

---


#### 문항 3

다음 문제의 빈칸의 숫자를 채워 넣으시오 (15 점)

The Influence of Learning Styles on Learners in E-Learning Environments: An Empirical Study by Manochehr, N. N.

Goal: The purpose of this study is two-fold: (1) to compare the effects of e-learning vs. those of traditional instructor-based learning on student learning, based on student learning styles; and (2) to determine if e-learning is more effective for those with a particular learning style.

Experiment Design: According to the Kolb LSI, there are learning styles of students. Kolb’s learning styles are defined by four levels: Diverger, Assimilator, Accommodator and Converger. The learning method was made up of two levels: e-learning and traditional learning. The student knowledge was analyzed in a 4 (LS: Learning Style) X 2 (LM: Learning Method) ANOVA

Learning Style: 1=Assimilator; 2=Diverger; 3=Accommodator; 4=Converger  
Method: IBL = instructor based learning (traditional); WBL = web based learning (e-learning)

Table 2. Summary of ANOVA for student knowledge

| Source | SOS | df | MS | F | p | $\eta^2$ |
|---|---:|---:|---:|---:|---:|---:|
| LS | 3299.24 | 3 | 1099.75 | 2.74 | .048 | .085 |
| LM | 96.63 | 1 | 96.63 | .24 | .625 | .002 |
| LS*LM | 1961.08 | 3 | 653.69 | 1.63 | .189 | .050 |
| Error | 34530.11 | 86 | 401.51 |  |  |  |
| Total | 38836.66 | 93 |  |  |  |  |

Note: SOS = sum of squares; df = degree of freedom; MS = mean square; F = computed F-value; p = level of significance.

[image: interaction plot of estimated marginal means of knowledge across learning styles 1-4 for IBL and WBL; the two lines differ by style and cross near style 4]

Figure 2. Interaction effects of learning style and learning method on student knowledge

Learning Style: 1=Assimilator;2=Diverger;3=Accommodator;4=Converger  
Method: IBL = instructor based learning (traditional); WBL = web based learning (e-learning)

The first F value is concerned with the main effect, which dealt with the learning styles. The two-way ANOVA, with student knowledge (grade score) identified correctly as the dependent variable, yielded a significant main effect for learning style [F $(????, ?????) = ????, p = ????$].

This means that learning style main effects are statistically significant in the student knowledge grade. Therefore, based upon the data collected and analysed in Table 2, there was a significant difference in student knowledge based on learning styles when learning on the web versus instructor-led. The Learning methods were not significant as the F value is p = ????. The interaction of learning styles and learning methods were $(significant????/not\ significant????)$ $(p = ????)$.

The e-learning mean was 60.78 (SD = 22.59) and the IBL mean was 62.28 (SD = 19.18). The means and standard deviations for both groups were not significantly different, giving some confidence that they represented the same population. At the same time, this finding confirms earlier findings that delivery strategy $(does????/does\ not????)$ significantly impact student outcome. If this is true, then the use of web-based strategies should be based on other factors.

---

#### 해설

- 표의 첫 번째 F값은 learning style의 주효과를 의미하므로 빈칸은
  $$F(3,86)=2.74,\ p=.048$$
  이다.
- 여기서 df `3`은 learning style이 4수준이므로 `4-1`, error df `86`은 표에 주어진 값 그대로 읽으면 된다.
- 따라서 학생 지식 점수는 학습스타일에 따라 유의하게 달라질 수 있다고 해석한다.
- 반면 learning method의 p값은 `.625` 이므로 유의하지 않다. 즉 WBL과 IBL의 평균 차이만 놓고 보면 통계적으로 뚜렷한 차이를 확인하기 어렵다.
- interaction의 p값은 `.189` 이고 이는 `not significant` 이다. 따라서 특정 learning style에서만 e-learning이 특별히 더 효과적이라고 단정할 증거도 부족하다.
- 마지막 빈칸은 delivery strategy가 student outcome에 유의한 영향을 `does not` 준다고 채우는 것이 맞다. 즉 성과 차이의 핵심은 전달방식 자체보다 learning style 쪽에 더 가깝다.

---


#### 문항 4

다음과 같은 세가지 그룹에 대해서 One-way ANOVA 검정을 RM 인 경우와 RM 인 아닌 경우 각각 실시하고 빈칸을 채우시오. (15 점)

##### 데이터

| Subject | A | B | C |
|---|---|---|---|
| 1 | 1 | 2 | 4 |
| 2 | 2 | 2 | 4 |
| 3 | 3 | 3 | 8 |
| 4 | 4 | 3 | 8 |
| **$\sum X$** | **10** | **10** | **24** |
| **Mean** | **2.5** | **2.5** | **6** |
| **$\sum X^2$** | **30** | **26** | **160** |

##### RM 이 아닌 경우

| Source | SS | Df | MS | F | p |
|---|---|---|---|---|---|
| Between Group | SS = ? | $df_{bg}$ = ? | $MS_{bg}$ = ? | $F(?, ?) = ?$ | 0.017 |
| Error | $SS_{error}$ = ? | $df_{error}$ = ? | $MS_{error}$ = ? | | |
| Total | SS = 54.67 | $df_T$ = ? | | | |

##### RM 인 경우

| Source | SS | Df | MS | F | p |
|---|---|---|---|---|---|
| Between Group | SS = ? | $df_{bg}$ = ? | $MS_{bg}$ = ? | $F(?, ?) = ?$ | 0.003 |
| Subject | $SS_{subject}$ = ? | $df_{subject}$ = ? | | | |
| Error | $SS_{error}$ = ? | $df_{error}$ = ? | $MS_{error}$ = ? | | |
| Total | SS = 54.67 | $df_T$ = ? | | | |

---

#### 해설

- 총합은 `44`, 전체평균은
  $$\bar x=44/12=3.6667$$
- 총제곱합은
  $$
  SS_T=216-\frac{44^2}{12}=54.6667
  $$
- 집단제곱합은
  $$
  SS_{bg}=\frac{10^2}{4}+\frac{10^2}{4}+\frac{24^2}{4}-\frac{44^2}{12}=32.6667
  $$
- RM이 아닌 경우:
  $$
  SS_{error}=54.6667-32.6667=22.0,\quad df_{bg}=2,\quad df_{error}=9,\quad df_T=11
  $$
  $$
  MS_{bg}=16.3333,\quad MS_{error}=22/9=2.4444
  $$
  $$
  F(2,9)=16.3333/2.4444\approx 6.6818
  $$
  따라서 p는 약 `0.017`이다.
- RM인 경우 subject 합은 `7,8,14,15` 이므로
  $$
  SS_{subject}=\frac{7^2+8^2+14^2+15^2}{3}-\frac{44^2}{12}=16.6667
  $$
  $$
  SS_{error}=54.6667-32.6667-16.6667=5.3333
  $$
  $$
  df_{subject}=3,\quad df_{error}=6,\quad df_T=11
  $$
  $$
  MS_{error}=5.3333/6=0.8889
  $$
  $$
  F(2,6)=16.3333/0.8889=18.375
  $$
- 따라서 RM 분석에서는 p가 약 `0.003`으로 더 작아진다. 반복측정 구조를 반영하면 개인차를 분리해 error가 줄어들기 때문이다.

---


#### 문항 5

다음은 수업시간에 다룬 Huang & Fu 의 "Don't Hide in the Crowd! Increasing Social Transparency Between Peer Workers Improves Crowdsourcing Outcomes" 의 일부이다. 빈칸(???로 표시)을 채우고 각 F 값이 의미하는 바를 Figure 4 를 이용하여 "자세하게" 설명하시오 (15 점)

> **Result**
>
> 300 subjects (50 subjects per treatment) were recruited from AMT; each of them completed 10 noun counting tasks and generated 10 labels; therefore, 3,000 labels (500 labels per treatment) were collected for our results analysis.
>
> We conducted a 3X2 Two-Way ANOVA to see if there were significant effects from the peer-dependent reward schemes, social transparency levels, and their interaction. The results showed that social transparency level did significantly affect the performance of workers (F(???, ???) = 7.58, p < 0.01)). However, the effect of peer-dependent reward schemes was not significant (F(???, ???) = 1.41, p = 0.24). Moreover, the effect of the interactions between the two factors was also insignificant (F(???, ???) = 1.26, p = 0.28).

[image: Figure 4. The mean of the average label accuracies of the workers under different peer-dependent reward schemes and social transparency levels (with standard error). In general, the workers who revealed their demographic information outperformed the ones who worked anonymously.]

|   | Anonymous | Demographic information revealed |
|---|---:|---:|
| Individual | 80.5% | 81.5% |
| Teamwork | 81.0% | 88.4% |
| Competition | 80.3% | 87.9% |
| Overall | 80.6% | 85.9% |

---

#### 해설

- 3×2 between-subject ANOVA 이고 각 셀에 50명씩 있으므로 총 표본수는
  $$N=3\times 2\times 50=300$$
- 자유도는
  $$
  df_{\text{reward}}=3-1=2,\quad df_{\text{transparency}}=2-1=1,\quad df_{\text{interaction}}=(3-1)(2-1)=2
  $$
  $$
  df_{error}=300-6=294
  $$
- 따라서 빈칸은
  - social transparency: `F(1,294)=7.58, p<.01`
  - peer-dependent reward schemes: `F(2,294)=1.41, p=.24`
  - interaction: `F(2,294)=1.26, p=.28`
- Figure 4에서 anonymous 평균은 전체적으로 `80.6%`, demographic information revealed 평균은 `85.9%`이다.
- 조건별로 보아도
  - Individual: `80.5% -> 81.5%`
  - Teamwork: `81.0% -> 88.4%`
  - Competition: `80.3% -> 87.9%`
  로 모두 투명성 공개 조건이 더 높다.
- 따라서 유의한 것은 `social transparency level`의 주효과이고, 평균 정확도는 demographic information이 공개된 조건에서 더 `higher`하다. 반면 reward scheme과 interaction은 유의하지 않으므로, 정확도와 관련된 핵심 요인은 보상방식이 아니라 사회적 투명성이라고 해석한다.

---


#### 문항 6

다음과 같은 세가지 그룹에 대해서 One-way ANOVA 검정을 RM 인 경우와 RM 인 아닌 경우 각각 실시하고 빈칸을 채우시오. (15 점)

| Subject | A | B | C |
|---|---:|---:|---:|
| 1 | 0 | 2 | 2 |
| 2 | 0 | 2 | 2 |
| 3 | 1 | 2 | 4 |
| 4 | 3 | 2 | 4 |

- A: $\sum X = 4$, Mean = 1, $\sum X^2 = 10$
- B: $\sum X = 8$, Mean = 2, $\sum X^2 = 16$
- C: $\sum X = 12$, Mean = 3, $\sum X^2 = 40$

**Within Subject Design**

| Source | SS | Df | MS | F | p |
|---|---|---|---|---|---|
| Between Group | $SS_{bg} = ?$ | $df_{bg} = ?$ | $MS_{bg} = ?$ | $F(?, ?) = ?$ | 0.037 |
| Subject | $SS_{subject} = ?$ | $df_{subj} = ?$ |  |  |  |
| Error | $SS_{error} = ?$ | $df_{error} = ?$ | $MS_{error} = ?$ |  |  |
| Total | $SS_T = 18$ | $df_T = ?$ |  |  |  |

**Between Subject Design**

| Source | SS | Df | MS | F | p |
|---|---|---|---|---|---|
| Between Group | $SS_{bg} = ?$ | $df_{bg} = ?$ | $MS_{bg} = ?$ | $F(?, ?) = ?$ | 0.07 |
| Error | $SS_{error} = ?$ | $df_{error} = ?$ | $MS_{error} = ?$ |  |  |
| Total | $SS_T = 18$ | $df_T = ?$ |  |  |  |

---

#### 해설

- 전체합은 `24`, 전체평균은 `2`이다.
- 총제곱합은
  $$
  SS_T=66-\frac{24^2}{12}=18
  $$
- 집단제곱합은
  $$
  SS_{bg}=\frac{4^2}{4}+\frac{8^2}{4}+\frac{12^2}{4}-\frac{24^2}{12}=8
  $$
- Within-subject design에서는 subject 합이 `4, 4, 7, 9` 이므로
  $$
  SS_{subject}=\frac{4^2+4^2+7^2+9^2}{3}-\frac{24^2}{12}=6
  $$
  $$
  SS_{error}=18-8-6=4
  $$
  자유도는 $df_{bg}=2$, $df_{subj}=3$, $df_{error}=6$, $df_T=11$ 이다.
  $$
  MS_{bg}=8/2=4,\qquad MS_{error}=4/6=0.6667
  $$
  $$
  F(2,6)=4/0.6667=6.0
  $$
- Between-subject design에서는
  $$
  SS_{error}=18-8=10,\qquad df_{error}=9,\qquad MS_{error}=10/9=1.1111
  $$
  $$
  F(2,9)=4/1.1111=3.6
  $$
- 따라서 같은 데이터라도 repeated structure를 반영한 분석이 더 큰 F 값을 준다.

---


#### 문항 7

다음과 같이 실험계획을 하고 Two-way Mixed ANOVA 분석을 수행하고자 하였다. 실험은 3 X 3 으로 두가지 A 와 B factor 를 사용하였다. A 조건은 between condition (randomized) 로 세가지가 있으며, B 조건은 repeated 조건으로 세가지 조건. Participants 은 모두 15 명으로 A 의 각 조건에 5 명씩 참여하였다. 이때 이러한 실험은 세가지의 가설을 검정할 수 있다. 세가지 (1)가설과, 각 검정에 사용하여야 하는 (2)자유도, 구하는 (3) F 값의 형식을 예와 같이 서술하시오. (10 점)

예) 가설: A 의 영향은 없다. F 값: F = MSA / MSA x B , 자유도: F(5, 50). (주의: 얘가 정답은 아님)

| A | A/S | B | A X B | B X A/S |
|---|---|---|---|---|

| Degrees of freedom | 20% (0.20) | 10% (0.10) | 5% (0.05) | 2% (0.02) | 1% (0.01) | 0.1% (0.001) |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3.078 | 6.314 | 12.706 | 31.821 | 63.657 | 636.619 |
| 2 | 1.886 | 2.920 | 4.303 | 6.965 | 9.925 | 31.598 |
| 3 | 1.638 | 2.353 | 3.182 | 4.541 | 5.841 | 12.941 |
| 4 | 1.533 | 2.132 | 2.776 | 3.747 | 4.604 | 8.610 |
| 5 | 1.476 | 2.015 | 2.571 | 3.365 | 4.032 | 6.859 |
| 6 | 1.440 | 1.943 | 2.447 | 3.143 | 3.707 | 5.959 |
| 7 | 1.415 | 1.895 | 2.365 | 2.998 | 3.499 | 5.405 |
| 8 | 1.397 | 1.860 | 2.306 | 2.896 | 3.355 | 5.041 |
| 9 | 1.383 | 1.833 | 2.262 | 2.821 | 3.250 | 4.781 |
| 10 | 1.372 | 1.812 | 2.228 | 2.764 | 3.169 | 4.587 |
| 11 | 1.363 | 1.796 | 2.201 | 2.718 | 3.106 | 4.437 |
| 12 | 1.356 | 1.782 | 2.179 | 2.681 | 3.055 | 4.318 |
| 13 | 1.350 | 1.771 | 2.160 | 2.650 | 3.012 | 4.221 |
| 14 | 1.345 | 1.761 | 2.145 | 2.624 | 2.977 | 4.140 |
| 15 | 1.341 | 1.753 | 2.131 | 2.602 | 2.947 | 4.073 |
| 16 | 1.337 | 1.746 | 2.120 | 2.583 | 2.921 | 4.015 |
| 17 | 1.333 | 1.740 | 2.110 | 2.567 | 2.898 | 3.965 |
| 18 | 1.330 | 1.734 | 2.101 | 2.552 | 2.878 | 3.922 |
| 19 | 1.328 | 1.729 | 2.093 | 2.539 | 2.861 | 3.883 |
| 20 | 1.325 | 1.725 | 2.086 | 2.528 | 2.845 | 3.850 |

---

#### 해설

- 3×3 mixed ANOVA 에서 A는 between factor 이고 B는 repeated factor 이다.
- 검정해야 할 세 가지 가설은
  - A의 주효과가 없다.
  - B의 주효과가 없다.
  - A와 B의 interaction이 없다.
- 참가자가 15명이고 A가 3수준이므로
  $$df_A=3-1=2,\qquad df_{S/A}=15-3=12$$
- B도 3수준 repeated factor 이므로
  $$df_B=3-1=2$$
  그리고 repeated 부분의 오차 자유도는
  $$df_{B\times S/A}=df_B\times df_{S/A}=2\times 12=24$$
- interaction 자유도는
  $$df_{AB}=(3-1)(3-1)=4$$
- 따라서 각 F형식은 다음과 같다.
  - A main effect:
    $$F=\frac{MS_A}{MS_{S/A}},\quad F(2,12)$$
  - B main effect:
    $$F=\frac{MS_B}{MS_{B\times S/A}},\quad F(2,24)$$
  - AB interaction:
    $$F=\frac{MS_{AB}}{MS_{B\times S/A}},\quad F(4,24)$$
- 이 문항의 핵심은 mixed design에서 between 효과와 repeated 효과가 서로 다른 error term을 사용한다는 점을 정확히 구분하는 것이다.

---


#### 문항 8

다음은 수업시간에 다룬 “NotiRing: A Comparative Study of Notification channel for Wearable Interactive Rings” by Roumen et al. 의 일부이다. ???에 들어 갈 숫자와 알맞은 말을 골라 쓰시오 (총 10 점)

Reaction time (s)

| Channel | Lying | Sitting | Standing | Walking | Running | Overall |
|---|---:|---:|---:|---:|---:|---:|
| Light | 2.45 | 3.22 | 2.87 | 2.93 | 2.86 | 2.87 |
| Sound | 1.79 | 1.84 | 1.63 | 1.85 | 1.68 | 1.76 |
| Vibration | 1.58 | 1.64 | 1.47 | 1.44 | 1.31 | 1.48 |
| Poke | 1.86 | 1.83 | 1.65 | 1.59 | 1.61 | 1.71 |
| Thermal | 14.79 | 13.94 | 13.93 | 14.91 | 13.66 | 14.23 |

Error rate (%)

| Channel | Lying | Sitting | Standing | Walking | Running | Overall |
|---|---:|---:|---:|---:|---:|---:|
| Light | 8% | 1.6% | 3.2% | 4.8% | 10.4% | 5.6% |
| Sound | 0% | 0% | 0% | 0.8% | 0% | 0.3% |
| Vibration | 0% | 0% | 0% | 1.6% | 0% | 0.8% |
| Poke | 2.4% | 0% | 0% | 3.2% | 4% | 1.9% |
| Thermal | 3.2% | 2.8% | 25.6% | 24% | 16% | 25.2% |

25 participants ranging from 20-35 years old (M = 23.8, SD = 3.1) volunteered for the study.

The experiment was a 5×5 within-subject design with two independent variables: channel (light, sound, vibration, poke, thermal) and activity level (lying down, sitting, standing, walking, running). We considered two dependent variables (DV): reaction time, error rate.

We found no significant main effect on activity level (p=.33), indicating that the error rate (??? does not or does) change much with different physical activities; however, channel did have a significant effect [F( ??? , ??? )=28.72; p<.001).

We also observed a channel × activity level interaction ( F( ??? , ??? ) =2.07; p<.01). This interaction was mainly apparent in two channels: the error rate of the thermal channel ( ??? : increased or decreased) as the intensity of activity increased, while light exhibited the opposite trend. These results show that our sensitivity to thermal stimuli ( ??? : increases or decreases) with physical activity. On the contrary, our ability to notice visual notifications decreases during increased activity.

---

#### 해설

- 5×5 within-subject design 이므로 channel 자유도는
  $$5-1=4$$
  activity level 자유도도
  $$5-1=4$$
  이다.
- 참가자가 25명이므로 repeated-measure error 자유도는
  $$4\times (25-1)=96$$
  이고, interaction 자유도는
  $$4\times 4=16$$
  이다.
- 따라서 빈칸은
  - activity level: error rate `does not` change much
  - channel main effect: `F(4,96)=28.72`
  - interaction: `F(16,384)=2.07`
- interaction error df `384`는
  $$16\times (25-1)=384$$
  로 계산된다.
- 표를 실제로 보면 thermal channel의 error rate는 low activity 구간보다 standing/walking 구간에서 훨씬 커진다. 즉 활동 강도가 커질수록 thermal channel performance는 전반적으로 악화된다고 보는 것이 맞다.
- 따라서 해당 빈칸은 thermal channel error가 `increased`, thermal stimuli에 대한 민감도는 `decreases`로 채우는 해석이 일관된다.

---


#### 문항 9

Two-way Mixed ANOVA 로 실험을 실시하였다 A 조건(Drug)은 세가지이며 Randomized 되어 있고 B 조건(Time)은 Repeated 로 네가지이다. 실험참가자는 모두 18 명으로 A 의 각 조건에 6 명씩 배정되었다. 이때 다음 표를 완성하시오. (10 점)

| Source | SS | Df | MS | F |
|---|---:|---:|---:|---|
| A (Drug) | 40 | ?? | ?? | F(?, ?) = ? |
| S/A | 15 | ?? | ?? |  |
| B (Time) | 5 | ?? | ?? | F(?, ?) = ? |
| AB (Interaction) | 10 | ?? | ?? | F(?, ?) = ? |
| B X S/A | ?? | ?? | ?? |  |
| Total | 100 | ?? |  |  |

---

#### 해설

- A는 3수준 between factor 이므로
  $$df_A=3-1=2$$
- 총 참가자 18명, 각 A 수준당 6명이므로 subject within A 자유도는
  $$df_{S/A}=18-3=15$$
- B는 4수준 repeated factor 이므로
  $$df_B=4-1=3$$
- interaction 자유도는
  $$df_{AB}=(3-1)(4-1)=6$$
- repeated factor 쪽 error 자유도는
  $$df_{B\times S/A}=15\times 3=45$$
- 총 자유도는
  $$df_T=18\times 4-1=71$$
- 주어진 SS를 이용하면
  $$
  SS_{B\times S/A}=100-(40+15+5+10)=30
  $$
- 평균제곱은
  $$
  MS_A=40/2=20,\quad MS_{S/A}=15/15=1
  $$
  $$
  MS_B=5/3=1.6667,\quad MS_{AB}=10/6=1.6667,\quad MS_{B\times S/A}=30/45=0.6667
  $$
- 따라서
  $$
  F_A(2,15)=20/1=20.0
  $$
  $$
  F_B(3,45)=1.6667/0.6667=2.5
  $$
  $$
  F_{AB}(6,45)=1.6667/0.6667=2.5
  $$

---


#### 문항 10

다음은 어느 세가지 그룹에 대해서 One-way ANOVA 검정을 RM 인 경우와 RM 인 아닌 경우 각각 실시하고 빈칸을 채우시오. (20 점)

| Subject | A | B | C | Total |
|---|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |  |
| 2 | 0 | 2 | 4 |  |
| 3 | 1 | 2 | 3 |  |
| 4 | 3 | 4 | 5 |  |

- A: $\Sigma X = 4$, 샘플평균 = 1, $\Sigma X^2 = 10$
- B: $\Sigma X = 8$, 샘플평균 = 2, $\Sigma X^2 = 24$
- C: $\Sigma X = 12$, 샘플평균 = 3, $\Sigma X^2 = 50$
- Total: $\Sigma X = 24$, 전체평균 = 2, $\Sigma X^2 = 84$

RM ANOVA

| Source | SS | Df | MS | F |
|---|---|---|---|---|
| Between Group | $SS_{bg} = ?$ | $df_{bg} = ?$ | $MS_{bg} = ?$ | $F(?, ?) = ?$ |
| Subject | $SS_{subject} = ?$ | $df_{subject} = ?$ |  |  |
| Error | $SS_{error} = ?$ | $df_{error} = ?$ | $MS_{error} = ?$ |  |
| Total | $SS_T = 36$ | $df_T = ?$ |  |  |

One-way ANOVA

| Source | SS | Df | MS | F |
|---|---|---|---|---|
| Between Group | $SS_{bg} = ?$ | $df_{bg} = ?$ | $MS_{bg} = ?$ | $F(?, ?) = ?$ |
| Error | $SS_{error} = ?$ | $df_{error} = ?$ | $MS_{error} = ?$ |  |
| Total | $SS_T = 36$ | $df_T = ?$ |  |  |

---

#### 해설

- 총제곱합은 문항에 주어진 대로 `36`이다.
- 집단제곱합은
  $$
  SS_{bg}=\frac{4^2}{4}+\frac{8^2}{4}+\frac{12^2}{4}-\frac{24^2}{12}=8
  $$
- RM ANOVA에서는 subject 합이 `0, 6, 6, 12` 이므로
  $$
  SS_{subject}=\frac{0^2+6^2+6^2+12^2}{3}-\frac{24^2}{12}=24
  $$
  $$
  SS_{error}=36-8-24=4
  $$
  $$
  df_{bg}=2,\quad df_{subject}=3,\quad df_{error}=6,\quad df_T=11
  $$
  $$
  MS_{bg}=4,\qquad MS_{error}=4/6=0.6667
  $$
  $$
  F(2,6)=4/0.6667=6.0
  $$
- One-way ANOVA에서는
  $$
  SS_{error}=36-8=28,\qquad df_{error}=9,\qquad MS_{error}=28/9\approx 3.1111
  $$
  $$
  F(2,9)=4/3.1111\approx 1.2857
  $$
- 따라서 반복측정 구조를 반영하면 같은 데이터에서도 error가 작아지고 F 값이 커진다.

---


#### 문항 11

다음 각 테스트에 대해서 수행할 수 있는 post hoc analysis 방법을 서술하세요. 여러가지가 가능한 경우는 하나만 써도 됩니다. (10 점)

1. One-way ANOVA (between subject design)
2. One-way RM ANOVA
3. Two-way RM ANOVA
4. Kruskal-Wallis test
5. Friedman test

---

#### 해설

- One-way ANOVA: `Tukey HSD`
- One-way RM ANOVA: `paired t-tests + Bonferroni/Holm`
- Two-way RM ANOVA: 유의한 interaction이 있으면 simple effects에 대한 paired comparison
- Kruskal-Wallis: `Dunn test`
- Friedman: `pairwise Wilcoxon signed-rank` 또는 `Nemenyi`
- Friedman: `pairwise Wilcoxon signed-rank` 또는 `Nemenyi`


## 11. 선형회귀, 상관, 회귀식 계산

- 선형회귀 문항은 회귀식을 쓰게 하는 수준에서 끝나지 않는다. slope와 intercept의 문맥 해석, residual 계산, SST/SSE/SSR 분해, R2 및 adjusted R2 계산까지 함께 묻는 경우가 반복된다.
- 좋은 출제는 작은 표본 데이터로 손으로 계산하게 하는 문제와, 실제 회귀 output table을 읽고 의미를 서술하게 하는 문제를 함께 섞는다.
- 학생들은 slope의 방향은 말해도 단위를 붙여 해석하지 못하거나, intercept를 의미 없는 값으로 넘기는 경우가 많다. 이 부분을 직접 쓰게 해야 한다.
- 상관계수와 공분산을 함께 구하게 하는 문항은 회귀 전 단계의 구조 이해를 확인하는 데 좋다. 변수 간 선형관계를 수치와 식으로 모두 표현하게 할 수 있다.
- 회귀 검정 문항에서는 H0 설정, t 통계량, rough p-value, 유의성 결론을 한 흐름으로 묻게 해야 회귀를 단순 예측식 암기로 푸는 것을 막을 수 있다.
- 손계산형 문항은 표본 수를 작게 유지하되, 합계와 제곱합을 제공해 계산 부담보다 구조 이해를 보게 하는 편이 좋다. 반대로 output 해석형 문항은 실제 데이터 맥락과 단위를 꼭 붙여야 한다.
- slope 해석에서는 `X가 1단위 증가할 때 Y가 평균적으로 얼마나 변하는가`를 문맥 단위와 함께 쓰게 해야 한다. 이 부분은 가장 자주 부분정답처럼 보이는 오답이 나오는 지점이다.
- intercept는 때로 실질적 해석이 약하다는 점까지 말할 수 있어야 한다. 무조건 숫자만 읽는 답과, 맥락상 한계를 짚는 답을 구분할 필요가 있다.
- 채점은 `회귀식`, `분산분해`, `계수 해석`, `잔차`, `결정계수`, `계수 검정`을 분리하는 것이 적절하다.
- 회귀 손계산 문항은 단순히 식만 맞추는지보다, $S_{xx}$, $S_{xy}$, SST, SSE, SSR의 관계를 끝까지 이어서 쓰는지를 봐야 한다. 중간값이 맞아도 구조가 틀린 답은 부분점수만 주는 편이 적절하다.
- output 해석형 문항은 slope의 부호만 읽지 말고 단위를 포함한 문맥 해석을 요구해야 한다. intercept는 해석 가능 여부 자체를 판단하게 하는 것도 좋다.
- $R^2$와 adjusted $R^2$를 함께 묻는 문항은 설명변수 개수가 늘어날 때 해석이 어떻게 달라지는지까지 확인할 수 있다. 단순 계산보다 지표의 역할 차이를 드러내는 해설형 소문항을 붙이면 효과적이다.

### 실제 문항

---


#### 문항 1

Perform linear regression analysis for the following data. (15 points)

| X | 1 | 1 | 2 | 2 |
|---|---|---|---|---|
| Y | 3 | 4 | 5 | 6 |

$\sum X = 6$, $\sum X^2 = 10$, $\sum Y = 18$, $\sum Y^2 = 86$, $\sum XY = 29$

1. Regression formula: $y = \beta_0 + \beta_1 * x$
2. $r^2$, SST, SSE, SSR, df
3. Error for the $\beta_1$
4. t-test for $\beta_1$

---

#### 해설

- 평균은
  $$\bar x=\frac{6}{4}=1.5,\qquad \bar y=\frac{18}{4}=4.5$$
- 중심화 제곱합은
  $$
  S_{xx}=\sum X^2-\frac{(\sum X)^2}{n}=10-\frac{36}{4}=1
  $$
  $$
  S_{xy}=\sum XY-\frac{(\sum X)(\sum Y)}{n}=29-\frac{6\cdot18}{4}=2
  $$
- 따라서
  $$
  \hat\beta_1=\frac{S_{xy}}{S_{xx}}=2,\qquad
  \hat\beta_0=\bar y-\hat\beta_1\bar x=4.5-2(1.5)=1.5
  $$
  이므로 회귀식은
  $$\hat y=1.5+2x$$
- 총제곱합은
  $$
  SST=\sum Y^2-\frac{(\sum Y)^2}{n}=86-\frac{18^2}{4}=5
  $$
- 회귀제곱합은
  $$
  SSR=\hat\beta_1 S_{xy}=2\cdot 2=4
  $$
- 잔차제곱합은
  $$
  SSE=SST-SSR=5-4=1
  $$
- 따라서
  $$
  r^2=\frac{SSR}{SST}=\frac45=0.8
  $$
- 오차분산 추정치는
  $$
  MSE=\frac{SSE}{n-2}=\frac12=0.5
  $$
  기울기 표준오차는
  $$
  SE(\hat\beta_1)=\sqrt{\frac{MSE}{S_{xx}}}=\sqrt{0.5}\approx 0.7071
  $$
- 기울기 검정통계량은
  $$
  t(2)=\frac{2}{0.7071}\approx 2.828
  $$
- p-value는 약 `0.106`이므로 5% 수준에서는 유의하지 않다.

---


#### 문항 2

다음 자료에 대해서 linear regression 분석을 하고 regression 식과 $r^2$ 를 구하시오 (5 점) 또한 Y 의 값이 X 값에 의해서 영향이 있는가를 통계적으로 분석하시오 (5 점)

|   | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| X | 0 | 0 | 1 | 1 |
| Y | 2 | 3 | 5 | 6 |

- $\sum X = 2$
- $\sum X^2 = 2$
- $\sum Y = 16$
- $\sum Y^2 = 74$
- $\sum XY = 11$

---

#### 해설

- 평균은
  $$\bar x=0.5,\qquad \bar y=4$$
- 중심화 제곱합은
  $$
  S_{xx}=2-\frac{2^2}{4}=1,\qquad
  S_{xy}=11-\frac{2\cdot16}{4}=3
  $$
- 따라서
  $$
  \hat\beta_1=3,\qquad \hat\beta_0=4-3(0.5)=2.5
  $$
  이므로 회귀식은
  $$\hat y=2.5+3x$$
- 총제곱합은
  $$
  SST=74-\frac{16^2}{4}=10
  $$
  회귀제곱합은
  $$SSR=3\cdot 3=9$$
  잔차제곱합은
  $$SSE=10-9=1$$
- 따라서
  $$
  r^2=\frac{9}{10}=0.9
  $$
- 기울기 표준오차는
  $$
  MSE=\frac{1}{2}=0.5,\qquad SE(\hat\beta_1)=\sqrt{0.5}=0.7071
  $$
- 검정통계량은
  $$
  t(2)=\frac{3}{0.7071}\approx 4.243
  $$
- df=2에서 5% 양측 기준값 4.303보다 약간 작으므로 p-value는 약 `0.051`이다. 따라서 5%에서는 기각하지 못하지만 매우 경계적이다.

---


#### 문항 3

Perform linear regression analysis for the following data. (15 points)

|   | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| X | -1 | 0 | 0 | 1 |
| Y | 3 | 1 | -1 | -1 |

- $\Sigma X = 0$
- $\Sigma X^2 = 2$
- $\Sigma Y = 2$
- $\Sigma Y^2 = 12$
- $\Sigma XY = -4$

1. Regression formula: $y = \mathrm{beta}_0 + \mathrm{beta}_1 * x$
2. $r^2$, SST, SSE, SSR
3. $H_0$ for t-test for beta$_1$
4. 통계량 t
5. 아래의 t-table 에서 5% 유의수준에 따른 기준이 되는 값
6. $H_0$ 를 기각한다 / 기각하지 못한다?

| Degrees of freedom (df) | .2 | .15 | .1 | .05 | .025 | .01 | .005 | .001 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3.078 | 4.165 | 6.314 | 12.706 | 25.452 | 63.657 | 127.321 | 636.619 |
| 2 | 1.886 | 2.282 | 2.920 | 4.303 | 6.205 | 9.925 | 14.089 | 31.599 |
| 3 | 1.638 | 1.924 | 2.353 | 3.182 | 4.177 | 5.841 | 7.453 | 12.924 |
| 4 | 1.533 | 1.778 | 2.132 | 2.776 | 3.495 | 4.604 | 5.598 | 8.610 |
| 5 | 1.476 | 1.699 | 2.015 | 2.571 | 3.163 | 4.032 | 4.773 | 6.869 |

---

#### 해설

- 평균은
  $$\bar x=0,\qquad \bar y=0.5$$
- 중심화 제곱합은
  $$
  S_{xx}=2,\qquad S_{xy}=-4
  $$
- 따라서
  $$
  \hat\beta_1=\frac{-4}{2}=-2,\qquad \hat\beta_0=0.5
  $$
  이므로 회귀식은
  $$\hat y=0.5-2x$$
- 총제곱합은
  $$
  SST=12-\frac{2^2}{4}=11
  $$
  회귀제곱합과 잔차제곱합은
  $$
  SSR=\hat\beta_1 S_{xy}=(-2)(-4)=8,\qquad SSE=11-8=3
  $$
- 따라서
  $$
  r^2=\frac{8}{11}\approx 0.7273
  $$
- 귀무가설은
  $$H_0:\beta_1=0$$
  이다.
- 오차분산과 기울기 표준오차는
  $$
  MSE=\frac{3}{2}=1.5,\qquad SE(\hat\beta_1)=\sqrt{\frac{1.5}{2}}=\sqrt{0.75}\approx 0.8660
  $$
- 따라서
  $$
  t(2)=\frac{-2}{0.8660}\approx -2.309
  $$
- df=2에서 5% 양측 기준값은 `4.303` 이므로 절댓값이 더 작다. 따라서 귀무가설을 기각하지 못한다.

---


#### 문항 4

다음 자료에 대해서 linear regression 분석을 하고 regression 식과 r2 를 구하시오. 또한 Y 의 값이 X 값에 의해서 영향을 받는가를 통계적으로 분석하시오 (총 10 점)

|   | -1 | 0 | 2 | 3 |
|---|---:|---:|---:|---:|
| X | -1 | 0 | 2 | 3 |
| Y | 3 | 1 | 0 | 0 |

- SX = 4
- SX2 = 14
- SY = 4
- SY2 = 10
- SXY = -3

1. Regression 식 = ?
2. r2 = ?
3. Adjusted r2 = ?
4. H0 (X 가 Y 에 영향을 미치는가에 대한 귀무가설): ?
5. t(?) = ?
6. p = ? (아래의 t-value table 을 이용하여 대략적인 값을 구하세요, 제시된 값은 양측검정 기준임을 유의하세요)

| Degrees of freedom | 20% (0.20) | 10% (0.10) | 5% (0.05) | 2% (0.02) | 1% (0.01) | 0.1% (0.001) |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3.078 | 6.314 | 12.706 | 31.821 | 63.657 | 636.619 |
| 2 | 1.886 | 2.920 | 4.303 | 6.965 | 9.925 | 31.598 |
| 3 | 1.638 | 2.353 | 3.182 | 4.541 | 5.841 | 12.941 |
| 4 | 1.533 | 2.132 | 2.776 | 3.747 | 4.604 | 8.610 |
| 5 | 1.476 | 2.015 | 2.571 | 3.365 | 4.032 | 6.859 |
| 6 | 1.440 | 1.943 | 2.447 | 3.143 | 3.707 | 5.959 |
| 7 | 1.415 | 1.895 | 2.365 | 2.998 | 3.499 | 5.405 |
| 8 | 1.397 | 1.860 | 2.306 | 2.896 | 3.355 | 5.041 |
| 9 | 1.383 | 1.833 | 2.262 | 2.821 | 3.250 | 4.781 |
| 10 | 1.372 | 1.812 | 2.228 | 2.764 | 3.169 | 4.587 |

---

#### 해설

- 평균은
  $$\bar x=1,\qquad \bar y=1$$
- 중심화 제곱합은
  $$
  S_{xx}=14-\frac{4^2}{4}=10,\qquad
  S_{xy}=-3-\frac{4\cdot4}{4}=-7
  $$
- 따라서
  $$
  \hat\beta_1=-7/10=-0.7,\qquad
  \hat\beta_0=1-(-0.7)(1)=1.7
  $$
  이므로 회귀식은
  $$\hat y=1.7-0.7x$$
- 총제곱합은
  $$
  SST=10-\frac{4^2}{4}=6
  $$
  회귀제곱합과 잔차제곱합은
  $$
  SSR=\hat\beta_1S_{xy}=(-0.7)(-7)=4.9,\qquad SSE=6-4.9=1.1
  $$
- 따라서
  $$
  r^2=\frac{4.9}{6}\approx 0.8167
  $$
  조정 결정계수는
  $$
  R^2_{adj}=1-\frac{SSE/(n-2)}{SST/(n-1)}
  =1-\frac{1.1/2}{6/3}=1-0.275=0.725
  $$
- 귀무가설은
  $$H_0:\beta_1=0$$
- 오차분산과 표준오차는
  $$
  MSE=1.1/2=0.55,\qquad SE(\hat\beta_1)=\sqrt{\frac{0.55}{10}}\approx 0.2345
  $$
- 따라서
  $$
  t(2)=\frac{-0.7}{0.2345}\approx -2.985
  $$
- df=2에서 p-value는 `0.10과 0.05 사이`이므로 5% 수준에서는 유의하지 않다.

---


#### 문항 5

다음 자료에 대해서 linear regression 분석을 하고 regression 식과 $r^2$ 를 구하시오. 또한 Y 의 값이 X 값에 의해서 영향을 받는가를 통계적으로 분석하시오 (총 15 점)

|   | 0 | 0 | 1 | 3 |
|---|---:|---:|---:|---:|
| X | 0 | 0 | 1 | 3 |
| Y | 1 | 1 | -1 | -1 |

1. Regression 식 = ?
2. $r^2$ = ?
3. Adjusted $r^2$ = ?
4. H0 (X 가 Y 에 미치는가에 대한 귀무가설): ?
5. (4)를 위한 통계량 t(?) = ?
6. (5)의 p = ? (아래의 표를 이용하여 대략적인 값을 구하면 됨)

| Degrees of freedom | 20% (0.20) | 10% (0.10) | 5% (0.05) | 2% (0.02) | 1% (0.01) | 0.1% (0.001) |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3.078 | 6.314 | 12.706 | 31.821 | 63.657 | 636.619 |
| 2 | 1.886 | 2.920 | 4.303 | 6.965 | 9.925 | 31.598 |
| 3 | 1.638 | 2.353 | 3.182 | 4.541 | 5.841 | 12.941 |
| 4 | 1.533 | 2.132 | 2.776 | 3.747 | 4.604 | 8.610 |
| 5 | 1.476 | 2.015 | 2.571 | 3.365 | 4.032 | 6.859 |
| 6 | 1.440 | 1.943 | 2.447 | 3.143 | 3.707 | 5.959 |
| 7 | 1.415 | 1.895 | 2.365 | 2.998 | 3.499 | 5.405 |
| 8 | 1.397 | 1.860 | 2.306 | 2.896 | 3.355 | 5.041 |
| 9 | 1.383 | 1.833 | 2.262 | 2.821 | 3.250 | 4.781 |
| 10 | 1.372 | 1.812 | 2.228 | 2.764 | 3.169 | 4.587 |

---

#### 해설

- 평균은
  $$\bar x=1,\qquad \bar y=0$$
- 중심화 제곱합은
  $$
  S_{xx}=10-\frac{4^2}{4}=6,\qquad
  S_{xy}=-4-\frac{4\cdot 0}{4}=-4
  $$
- 따라서
  $$
  \hat\beta_1=-4/6=-0.6667,\qquad \hat\beta_0=0-(-0.6667)(1)=0.6667
  $$
- 회귀식은
  $$\hat y=0.6667-0.6667x$$
- 총제곱합은
  $$
  SST=4-\frac{0^2}{4}=4
  $$
  회귀제곱합과 잔차제곱합은
  $$
  SSR=\hat\beta_1S_{xy}=2.6667,\qquad SSE=4-2.6667=1.3333
  $$
- 따라서
  $$
  r^2=2.6667/4=0.6667
  $$
  조정 결정계수는
  $$
  R^2_{adj}=1-\frac{SSE/(n-2)}{SST/(n-1)}
  =1-\frac{1.3333/2}{4/3}=0.5
  $$
- 기울기 검정은
  $$
  MSE=1.3333/2=0.6667,\qquad SE(\hat\beta_1)=\sqrt{0.6667/6}=0.3333
  $$
  $$
  t(2)=\frac{-0.6667}{0.3333}=-2.0
  $$
- 따라서 p-value는 `0.20과 0.10 사이`이고, 5% 수준에서는 유의하지 않다.

---


#### 문항 6

다음 두 sequence 의 Corr(X, Y), Cov(X, Y), Simple Regression Model 을 구하시오

| X | Y |
|---|---|
| 10 | 8 |
| 8 | 6 |
| 13 | 7 |
| 9 | 8 |
| 11 | 8 |
| 14 | 9 |
| 6 | 7 |
| 4 | 4 |
| 7 | 4 |
| 4 | 4 |

---

#### 해설

- 평균은
  $$\bar x=\frac{86}{10}=8.6,\qquad \bar y=\frac{65}{10}=6.5$$
- 편차곱의 합은
  $$
  \sum (x_i-\bar x)(y_i-\bar y)=48.0
  $$
  이므로 표본공분산은
  $$
  Cov(X,Y)=\frac{48.0}{10-1}=5.3333
  $$
- 또한
  $$
  S_{xx}=\sum (x_i-\bar x)^2=92.4,\qquad
  S_{yy}=\sum (y_i-\bar y)^2=42.5
  $$
  이므로 상관계수는
  $$
  r=\frac{48.0}{\sqrt{92.4\cdot 42.5}}\approx 0.8087
  $$
- 단순회귀의 기울기는
  $$
  \hat\beta_1=\frac{48.0}{92.4}\approx 0.5195
  $$
  절편은
  $$
  \hat\beta_0=6.5-0.5195(8.6)\approx 2.0325
  $$
- 따라서 simple regression model은
  $$\hat y=2.0325+0.5195x$$
  이다.

---


#### 문항 7

The following table presents regression output from a model for predicting annual murders per million from percentage living in poverty based on a random sample of 20 metropolitan areas. The model output is also provided below (10 점).

|   | Estimate | Std. Error | t value | Pr(>\|t\|) |
|---|---:|---:|---:|---:|
| (Intercept) | -29.901 | 7.789 | -3.839 | 0.001 |
| poverty% | 2.559 | 0.390 | 6.562 | 0.000 |

- $s = 5.512$
- $R^2 = 70.52\%$
- $R^2_{adj} = 68.89\%$

[image: scatterplot of annual murder rate versus percent in poverty showing a clear positive linear trend]

1. Write out the linear model
2. Interpret the intercept
3. Interpret the slope
4. What are the hypotheses for evaluating whether poverty percentage is a significant predictor of murder rate?
5. State the conclusion of the hypothesis test from part (a) in context of the data.
6. Calculate a 95% confidence interval for the slope of poverty percentage, and interpret it in context of the data. (6 번 문제에 제공되는 t-값 테이블을 사용하세요)
7. Do your results from the hypothesis test and the confidence interval agree? Explain.

---

#### 해설

- 선형모형은
  $$
  \widehat{\text{murders}}=-29.901+2.559\cdot poverty\%
  $$
- 절편 `-29.901`은 빈곤율이 0%일 때 예측 murder rate를 뜻한다. 다만 실제 자료 범위 밖이면 실질적 해석은 제한적일 수 있다.
- slope `2.559`는 빈곤율이 1%p 증가할 때 연간 백만 명당 murders가 평균 `2.559`만큼 증가한다고 해석한다.
- 기울기 유의성 검정의 가설은
  $$H_0:\beta_1=0,\qquad H_A:\beta_1\ne 0$$
- 출력에서
  $$t=6.562,\quad p<0.001$$
  이므로 빈곤율은 murder rate의 유의한 예측변수다.
- 95% 신뢰구간은 df=`20-2=18`에서 $t^*\approx 2.101$을 쓰면
  $$
  2.559\pm 2.101(0.390)=2.559\pm 0.819
  $$
  즉
  $$
  (1.740,\ 3.378)
  $$
  이다.
- 이 구간이 0을 포함하지 않으므로, 가설검정 결과와 신뢰구간 결과는 서로 일치한다.

---


#### 문항 8

Researchers interested in the relationship between absenteeism (무단결석) from school and certain demographic characteristics of children collected data from 146 randomly sampled students in a country. Below are three observations from the data set. (참고: aboriginal = 원주민) (10 points)

|   | eth | sex | lrn | days |
|---|---:|---:|---:|---:|
| 1 | 0 | 1 | 1 | 2 |
| 2 | 0 | 1 | 1 | 11 |
| ... | ... | ... | ... | ... |
| 146 | 1 | 0 | 0 | 37 |

The summary table below shows the results of a linear regression model for predicting the average number of days absent based on ethnic background (eth: 0 - aboriginal, 1 - not aboriginal), sex (sex: 0 - female, 1 - male), and learner status (lrn: 0 - average learner, 1 - slow learner).

|   | Estimate | Std. Error | t value | Pr(>\|t\|) |
|---|---:|---:|---:|---:|
| (Intercept) | 18.93 | 2.57 | 7.37 | 0.0000 |
| eth | -9.11 | 2.60 | -3.51 | 0.0000 |
| sex | 3.10 | 2.64 | 1.18 | 0.2411 |
| lrn | 2.15 | 2.65 | 0.81 | 0.4177 |

(a) Write the equation of the regression line.

(b) Interpret each one of the slopes in this context.

(c) Calculate the residual for the first observation in the data set: a student who is aboriginal, male, a slow learner, and missed 2 days of school.

(d) The variance of the residuals is 240.57, and the variance of the number of absent days for all students in the data set is 264.17. Calculate the $R^2$ and the adjusted $R^2$. Note that there are 146 observations in the data set.

---

#### 해설

- 회귀식은
  $$
  \hat y=18.93-9.11\,eth+3.10\,sex+2.15\,lrn
  $$
- 각 기울기 해석:
  - `eth=-9.11`: 다른 변수가 같을 때, not aboriginal(`eth=1`) 학생은 aboriginal(`eth=0`) 학생보다 결석일수가 평균 `9.11일` 적다.
  - `sex=3.10`: 다른 변수가 같을 때, 남학생(`sex=1`)은 여학생(`sex=0`)보다 평균 `3.10일` 더 결석한다고 예측된다.
  - `lrn=2.15`: 다른 변수가 같을 때, slow learner(`lrn=1`)는 average learner(`lrn=0`)보다 평균 `2.15일` 더 결석한다고 예측된다.
- 첫 번째 관측치는 `eth=0, sex=1, lrn=1` 이므로 예측값은
  $$
  \hat y=18.93-9.11(0)+3.10(1)+2.15(1)=24.18
  $$
- 실제값이 2일이므로 residual은
  $$
  e=y-\hat y=2-24.18=-22.18
  $$
- 분산 정보를 이용하면
  $$
  R^2=1-\frac{240.57}{264.17}\approx 0.0893
  $$
- 설명변수 개수 $p=3$, 표본수 $n=146$ 이므로 adjusted $R^2$는
  $$
  1-(1-R^2)\frac{n-1}{n-p-1}
  =1-(1-0.0893)\frac{145}{142}
  \approx 0.0701
  $$


## 12. 회귀 가정, 이상치, 모형 선택

- 이 개념은 계산형보다는 `이 모델을 믿어도 되는가`를 묻는 축이다. regression assumptions, collinearity, adjusted R2, extrapolation, leverage, influence, backward elimination 등이 여기에 포함된다.
- 실제 시험에서는 이 주제가 독립된 장문 문항으로 나오기도 하지만, 더 자주 나오는 형태는 용어 설명 묶음 안에 섞여 있는 방식이다. 따라서 학생이 맥락 없이도 정확한 정의를 말할 수 있어야 한다.
- 좋은 문항은 high leverage point와 influential point를 구분시키거나, adjusted R2가 왜 필요한지, backward elimination의 기준을 어떻게 잡는지처럼 모델 선택 사고를 요구한다.
- 또한 회귀선 밖으로 예측하는 extrapolation의 위험성과 collinearity가 계수 해석에 주는 문제를 실제 데이터 맥락과 연결하게 하면 깊이가 생긴다.
- 채점에서는 단어 정의만이 아니라, 그 개념이 회귀 결과의 신뢰성과 해석 가능성에 어떤 영향을 주는지까지 설명했는지를 봐야 한다.
- 이 섹션은 계산보다 판단이 중요하므로, `가정 이름`만 쓰게 하기보다 가정이 깨지면 어떤 해석 문제가 생기는지를 같이 쓰게 해야 한다.
- outlier 관련 문항은 high leverage, large residual, influential observation을 구분하게 해야 한다. 세 개를 같은 뜻처럼 아는 학생이 매우 많다.
- model selection 문항은 adjusted $R^2$, AIC/BIC, backward elimination을 서로 연결해 묻는 편이 효과적이다. 단순 정의보다는 왜 변수를 줄이려 하는지까지 설명하게 해야 한다.
- 채점은 `정의`, `위배 시 문제`, `실제 진단 목적`, `대안 또는 보정 방법`을 기준으로 나누는 것이 좋다.

### 실제 문항

---


#### 문항 1

Linear regression 을 수행하기 위해 데이터가 만족해야하는 세가지 조건에 대해서 구체적으로 설명하시오 (5 점)

---

#### 해설

- 선형회귀에서 가장 기본적인 가정은 explanatory variable 과 response variable 사이 관계가 선형적이라는 점이다.
- 또한 오차는 서로 독립이어야 하고, 예측값 범위 전반에 걸쳐 분산이 비슷한 등분산성을 가져야 하며, 잔차는 대체로 정규성을 만족하는 것이 바람직하다.
- 여기에 더해, 아주 강한 leverage point 나 influential point 가 있으면 회귀계수와 예측이 심하게 왜곡될 수 있다.
- 따라서 회귀모형의 타당성을 판단할 때는 단순히 계수값만 볼 것이 아니라, residual plot, QQ plot, leverage 진단 등을 함께 봐야 한다.


## 13. 범주형 자료, Chi-square, confusion matrix

- 이 섹션은 범주형 자료의 독립성 검정과 분류 성능 요약을 다룬다. contingency table, chi-square independence, goodness of fit, confusion matrix, sensitivity/specificity가 핵심이다.
- 좋은 문제는 셀 빈도를 기반으로 검정통계량을 계산하게 한 뒤, 단순 유의성 판정이 아니라 어떤 관계가 있다고 말할 수 있는지 문맥 속 결론을 쓰게 한다.
- confusion matrix 문항은 Accuracy 하나로 끝내지 않고 Precision, Recall, F1, Sensitivity, Specificity를 각각 어떤 상황에서 더 중요하게 볼 수 있는지 연결하면 해석력이 드러난다.
- 학생들은 chi-square의 tail 해석, 자유도, expected count의 의미를 자주 놓친다. 참/거짓형과 표 계산형을 섞으면 이 오개념을 잘 걸러낼 수 있다.
- 범주형 치료 효과 문항에서는 생존/사망, 선호도 차이처럼 실제 맥락을 제시하고, 독립성 검정 또는 적절한 범주형 비교 방법을 선택하게 하는 구성이 적합하다.
- 출제에서는 표 구조, 기대도수, 자유도, 관련성 해석을 함께 확인할 수 있어야 한다.
- 학생들은 chi-square가 항상 양측검정이라고 오해하거나, 기대도수를 관측도수처럼 해석하는 경우가 많다. 이런 부분은 짧은 판단형 문항으로 함께 확인하는 것이 좋다.
- confusion matrix는 식만 외우는 학생이 많으므로, precision과 recall이 왜 다른지, 어떤 오분류가 더 위험한 상황인지까지 연결하는 문항이 좋다.
- 채점은 `검정 선택`, `자유도`, `검정통계량`, `기각 여부`, `문맥 해석`, `분류지표 의미`를 분리해 보는 것이 적절하다.

### 실제 문항

---


#### 문항 1

다음 표는 분류작업에서 실제값과 예측값을 나타내는 confusion matrix 이다. 각 값의 계산식을 예제와 같이 표시하시오. (10 점)

|   | Total Population | Predicted Condition Positive | Predicted Condition Negative |
|---|---|---|---|
| Actual Condition Positive | Positive | True Positive (a) | False Negative (b) |
| Actual Condition Negative | Negative | False Positive (c) | True Negative (d) |

예) Accuracy = [ (a) + (d) ] / [ (a) + (b) + (c) + (d) ]

1. Precision
2. Recall
3. F1
4. Sensitivity
5. Specificity

---

#### 해설

- 문제의 표기대로 $TP=a$, $FN=b$, $FP=c$, $TN=d$ 로 두면 전체 표본수는
  $$N=a+b+c+d$$
- 각 지표는 다음과 같다.
  - Precision:
    $$\frac{a}{a+c}$$
  - Recall:
    $$\frac{a}{a+b}$$
  - F1:
    $$
    \frac{2\cdot Precision\cdot Recall}{Precision+Recall}
    =\frac{2a}{2a+b+c}
    $$
  - Sensitivity:
    $$\frac{a}{a+b}$$
  - Specificity:
    $$\frac{d}{c+d}$$
- Recall과 Sensitivity는 이 표에서는 같은 식이 된다. 반면 Precision은 `양성으로 예측한 것 중 얼마나 맞았는가`, Specificity는 `실제 음성 중 얼마나 음성으로 맞췄는가`를 본다는 점이 다르다.

---


#### 문항 2

다음 데이터는 어느 학교의 학생을 대상으로 학년에 따른 게임의 선호도를 조사한 결과이다. 이러한 데이터가 학년에 따라서 게임의 선호도가 달라진다는 증거로 사용될 수 있는가 통계적으로 분석하세요. 아래의 Chi-Square Table 을 사용하세요. (10 점)

| 학년 | LoL | Overwatch | PUBG |
|---|---:|---:|---:|
| 중1 | 6 | 7 | 7 |
| 중2 | 4 | 8 | 8 |
| 중3 | 10 | 5 | 5 |

| Upper tail df | 0.3 | 0.2 | 0.1 | 0.05 | 0.02 | 0.01 | 0.005 | 0.001 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 2.41 | 3.22 | 4.61 | 5.99 | 7.82 | 9.21 | 10.60 | 13.82 |
| 3 | 3.66 | 4.64 | 6.25 | 7.81 | 9.84 | 11.34 | 12.84 | 16.27 |
| 4 | 4.88 | 5.99 | 7.78 | 9.49 | 11.67 | 13.28 | 14.86 | 18.47 |
| 5 | 6.06 | 7.29 | 9.24 | 11.07 | 13.39 | 15.09 | 16.75 | 20.52 |

---

#### 해설

- 각 행합과 열합이 모두 `20`이고 전체합은 `60`이다. 따라서 모든 기대도수는
  $$
  E_{ij}=\frac{20\times 20}{60}=6.6667
  $$
  로 같다.
- chi-square 통계량은
  $$
  \chi^2=\sum \frac{(O-E)^2}{E}
  $$
  이고, 각 셀 기여도는 예를 들어
  $$
  \frac{(6-6.6667)^2}{6.6667}=0.0667,\quad
  \frac{(8-6.6667)^2}{6.6667}=0.2667,\quad
  \frac{(10-6.6667)^2}{6.6667}=1.6667
  $$
  이다.
- 전체를 더하면
  $$\chi^2\approx 4.20$$
- 자유도는
  $$
  df=(3-1)(3-1)=4
  $$
- 표에서 df=4, 0.30 upper-tail 값이 `4.88` 이므로 `4.20 < 4.88` 이다. 즉 p-value는 `0.30보다 크다`.
- 따라서 학년에 따라 게임 선호도가 달라진다고 말할 통계적 증거는 충분하지 않다.

---


#### 문항 3

다음과 같은 데이터는 어느 학교의 학생을 대상으로 학년에 따른 게임의 선호도를 조사한 결과이다. 이러한 데이터가 학년에 따라서 게임의 선호도가 달라진다는 증거로 사용될 수 있는가 통계적 분석을 실시하시오. (5 점)

| 학년 | LoL | Overwatch | Battle Ground | Sudden Attack | Total |
|---|---:|---:|---:|---:|---:|
| 중 1 | 10 | 10 | 10 | 10 | 40 |
| 중 2 | 5 | 15 | 15 | 5 | 40 |
| 중 3 | 15 | 5 | 5 | 15 | 40 |
| Total | 30 | 30 | 30 | 30 | 120 |

| Upper tail df | 0.3 | 0.2 | 0.1 | 0.05 | 0.02 | 0.01 | 0.005 | 0.001 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 2.41 | 3.22 | 4.61 | 5.99 | 7.82 | 9.21 | 10.60 | 13.82 |
| 3 | 3.66 | 4.64 | 6.25 | 7.81 | 9.84 | 11.34 | 12.84 | 16.27 |
| 4 | 4.88 | 5.99 | 7.78 | 9.49 | 11.67 | 13.28 | 14.86 | 18.47 |
| 5 | 6.06 | 7.29 | 9.24 | 11.07 | 13.39 | 15.09 | 16.75 | 20.52 |

---

#### 해설

- 각 행합은 `40`, 각 열합은 `30`, 전체합은 `120`이다.
- 따라서 모든 셀의 기대도수는
  $$
  E_{ij}=\frac{40\times 30}{120}=10
  $$
- 첫째 행은 관측도수와 기대도수가 모두 같으므로 기여도가 0이다.
- 둘째 행의 기여도는
  $$
  \frac{(5-10)^2}{10}+\frac{(15-10)^2}{10}+\frac{(15-10)^2}{10}+\frac{(5-10)^2}{10}
  =2.5+2.5+2.5+2.5=10
  $$
- 셋째 행도 동일하게 `10`이므로
  $$\chi^2=20$$
- 자유도는
  $$df=(3-1)(4-1)=6$$
- df=6에서 1% 임계값은 표에 `16.81`, 0.1% 임계값은 `22.46` 이다. 따라서 `20`은 그 사이에 있으므로 p-value는 `0.01보다 작고 0.001보다 크다`.
- 따라서 학년과 게임 선호도는 독립이라고 보기 어렵고, 학년에 따라 선호 패턴이 달라진다고 결론내린다.

---


#### 문항 4

다음은 어느 병원에서 심장이식을 받은 환자(treatment)와 그렇지 않은 환자(control)의 생존과 사망을 조사한 표이다. 심장이식이 생존율을 높인다고 할 수 있는가 통계적 검증을 수행하고, 가정이 필요하면 하고 이를 설명하세요. (10 점)

|   | control | treatment |
|---|---:|---:|
| alive | 4 | 24 |
| dead | 30 | 45 |

---

#### 해설

- 관측표는
  $$
  \begin{array}{c|cc}
   & control & treatment\\ \hline
  alive & 4 & 24\\
  dead & 30 & 45
  \end{array}
  $$
  이고 전체합은 `103`이다.
- 행합은 `28, 75`, 열합은 `34, 69` 이므로 기대도수는
  $$
  E=\begin{pmatrix}
  28\cdot34/103 & 28\cdot69/103\\
  75\cdot34/103 & 75\cdot69/103
  \end{pmatrix}
  \approx
  \begin{pmatrix}
  9.243 & 18.757\\
  24.757 & 50.243
  \end{pmatrix}
  $$
- chi-square 통계량은
  $$
  \chi^2=\sum \frac{(O-E)^2}{E}\approx 6.096
  $$
- 자유도는
  $$df=(2-1)(2-1)=1$$
- df=1에서 5% 임계값은 약 `3.84`, 1% 임계값은 약 `6.64` 이므로 이 결과는 5% 수준에서는 유의하고 1% 수준에서는 경계적이다.
- 생존률을 보면 control은 `4/34=11.8%`, treatment는 `24/69=34.8%` 이다. 따라서 심장이식군의 생존률이 더 높다고 볼 통계적 근거가 있다.

---


#### 문항 5

어떠한 처치(Therapy)에 대하여 예후가 다음과 같다. 이 처치가 효과가 있다고 얘기할 수 있는가? (10 점)

|   | Worse | N/C | Improved | Total |
|---|---:|---:|---:|---:|
| Therapy | 24 | 11 | 25 | 60 |
| No Therapy | 30 | 31 | 29 | 90 |
| Total | 54 | 42 | 54 | 150 |

< Chi-square p value table >

| Upper tail df | 0.3 | 0.2 | 0.1 | 0.05 | 0.02 | 0.01 | 0.005 | 0.001 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 2.41 | 3.22 | 4.61 | 5.99 | 7.82 | 9.21 | 10.60 | 13.82 |
| 3 | 3.66 | 4.64 | 6.25 | 7.81 | 9.84 | 11.34 | 12.84 | 16.27 |
| 4 | 4.88 | 5.99 | 7.78 | 9.49 | 11.67 | 13.28 | 14.86 | 18.47 |
| 5 | 6.06 | 7.29 | 9.24 | 11.07 | 13.39 | 15.09 | 16.75 | 20.52 |
| 6 | 7.23 | 8.56 | 10.64 | 12.59 | 15.03 | 16.81 | 18.55 | 22.46 |
| 7 | 8.38 | 9.80 | 12.02 | 14.07 | 16.62 | 18.48 | 20.28 | 24.32 |
| 8 | 9.52 | 11.03 | 13.36 | 15.51 | 18.17 | 20.09 | 21.95 | 26.12 |
| 9 | 10.66 | 12.24 | 14.68 | 16.92 | 19.68 | 21.67 | 23.59 | 27.88 |
| 10 | 11.78 | 13.44 | 15.99 | 18.31 | 21.16 | 23.21 | 25.19 | 29.59 |
| 11 | 12.90 | 14.63 | 17.28 | 19.68 | 22.62 | 24.72 | 26.76 | 31.26 |
| 12 | 14.01 | 15.81 | 18.55 | 21.03 | 24.05 | 26.22 | 28.30 | 32.91 |
| 13 | 15.12 | 16.98 | 19.81 | 22.36 | 25.47 | 27.69 | 29.82 | 34.53 |
| 14 | 16.22 | 18.15 | 21.06 | 23.68 | 26.87 | 29.14 | 31.32 | 36.12 |
| 15 | 17.32 | 19.31 | 22.31 | 25.00 | 28.26 | 30.58 | 32.80 | 37.70 |
| 16 | 18.42 | 20.47 | 23.54 | 26.30 | 29.63 | 32.00 | 34.27 | 39.25 |
| 17 | 19.51 | 21.61 | 24.77 | 27.59 | 31.00 | 33.41 | 35.72 | 40.79 |
| 18 | 20.60 | 22.76 | 25.99 | 28.87 | 32.35 | 34.81 | 37.16 | 42.31 |
| 19 | 21.69 | 23.90 | 27.20 | 30.14 | 33.69 | 36.19 | 38.58 | 43.82 |
| 20 | 22.77 | 25.04 | 28.41 | 31.41 | 35.02 | 37.57 | 40.00 | 45.31 |
| 25 | 28.17 | 30.68 | 34.38 | 37.65 | 41.57 | 44.31 | 46.93 | 52.62 |
| 30 | 33.53 | 36.25 | 40.26 | 43.77 | 47.96 | 50.89 | 53.67 | 59.70 |
| 40 | 44.16 | 47.27 | 51.81 | 55.76 | 60.44 | 63.69 | 66.77 | 73.40 |
| 50 | 54.72 | 58.16 | 63.17 | 67.50 | 72.61 | 76.15 | 79.49 | 86.66 |

---

#### 해설

- 전체합은 `150`, 행합은 `60, 90`, 열합은 `54, 42, 54` 이다.
- 기대도수는
  $$
  \begin{array}{c|ccc}
   & Worse & N/C & Improved\\ \hline
  Therapy & 21.6 & 16.8 & 21.6\\
  No\ Therapy & 32.4 & 25.2 & 32.4
  \end{array}
  $$
- chi-square 통계량은
  $$
  \chi^2=\sum \frac{(O-E)^2}{E}\approx 4.674
  $$
- 자유도는
  $$df=(2-1)(3-1)=2$$
- 표에서 df=2, 10% 임계값은 `4.61`, 5% 임계값은 `5.99` 이다. 따라서 `4.674`는 두 값 사이에 있으므로 p-value는 `0.10보다 작고 0.05보다 크다`.
- 따라서 5% 유의수준에서는 치료 효과가 있다고 말하기 어렵고, 10% 수준에서는 약한 증거 정도만 있다고 해석할 수 있다.


## 14. Logistic regression, Odds ratio, Relative risk, 분류기 평가

- 이 축은 로지스틱 회귀 output을 해석하고, coefficient를 odds ratio로 바꾸어 읽고, OR과 RR의 차이를 이해하는지를 평가한다.
- 기출에서는 Bird Keeping 예제처럼 실제 coefficient table을 주고 특정 변수가 사건 발생에 미치는 영향을 해석하게 하는 문제가 반복된다.
- 좋은 문항은 단순히 `유의하다`고 쓰게 하는 것이 아니라, 계수를 지수화했을 때 odds가 어떻게 변하는지, 이것이 relative risk와 왜 다른지를 문장으로 설명하게 해야 한다.
- 분류기 평가 문항은 logistic regression을 스팸 분류기나 분류모델 선택 문제와 연결해 ROC, 성능 비교, 최적 모델 선택 기준을 서술하게 할 때 효과적이다.
- 채점에서는 coefficient sign, p-value, OR 해석, RR과의 차이, 그리고 실제 적용 맥락까지 단계적으로 보는 것이 좋다.
- 학생들이 가장 자주 틀리는 부분은 coefficient 자체를 확률 변화량으로 읽는 것이다. 따라서 로그오즈, odds ratio, predicted probability의 차이를 단계적으로 구분하게 해야 한다.
- OR에서 RR로 넘어가는 문항은 특히 좋다. 사건이 드물 때는 비슷하지만 항상 같은 것은 아니라는 점을 설명하게 하면 개념 이해를 깊게 볼 수 있다.
- 분류기 평가 문항에서는 정확도만 말하는 답을 경계해야 한다. ROC, threshold, precision-recall tradeoff, out-of-sample validation 같은 요소를 함께 요구해야 실제 모델 선택 감각을 볼 수 있다.
- 채점은 `계수 부호 해석`, `exp(beta) 변환`, `문맥 서술`, `OR-RR 구분`, `모델 평가 기준`을 분리하는 편이 좋다.

### 실제 문항

---


#### 문항 1

스팸을 판별하는 classifier 를 logistic regression model 을 이용하여 구현하려 한다. 이때 여러 가장 좋은 성능을 가지는 모델을 정하는 방법에 대하여 서술하시오 (10 점)

---

#### 해설

- 로지스틱 회귀로 만든 분류기는 단순히 accuracy 하나로 평가하면 부족하다.
- 특히 실제 양성 탐지가 중요한 문제에서는 sensitivity 가 중요하고, 거짓 양성을 줄이는 것이 중요하면 specificity 가 더 중요할 수 있다.
- threshold 를 바꿔가며 성능을 보는 ROC curve 와 AUC 도 함께 확인해야 전체 분류 능력을 더 잘 판단할 수 있다.
- 또한 class imbalance 가 있는 자료에서는 다수집단만 잘 맞춰도 accuracy 가 높게 나올 수 있으므로, accuracy 만으로 좋은 모델이라고 결론내리면 안 된다.

---


#### 문항 2

수업시간에 다룬 바와 같이 다음은 새를 키우는 사람과 폐암발생 간의 관계를 logistic regression 으로 모델링한 예이다. 위 문항 2와 동일한 모델 결과를 이용하여 BK(Bird Keeping)가 LC(Lung Cancer)에 미치는 영향을 해석하시오.

Odds ratio 와 Relative risk 의 각각 정의를 서술하고 (5 점) 위 분석결과를 가지고 Odds ratio 를 통해 Relative risk 를 구하시오 (5 점) 이때 exp(1.36259) = 3.90, P(Lung cancer | No Birds) = 0.02 라고 가정하시오.

---

#### 해설

- Odds ratio 는 두 집단의 odds 를 비교한 비율이고, Relative risk 는 두 집단의 사건 발생 확률 자체를 비교한 비율이다.
- 따라서 OR은 확률을 직접 비교하는 값이 아니라, 확률을 odds 로 바꾼 뒤 그 비율을 본 것이라는 차이가 있다.
- 사건이 매우 드문 경우에는 OR 과 RR 이 비슷해질 수 있지만, 사건이 흔해질수록 OR 이 RR 보다 더 크게 보이는 경향이 있다.
- 여기서는 BK의 회귀계수가 `1.36259` 이므로
  $$
  OR=\exp(1.36259)=3.90
  $$
  이다. 즉 다른 변수가 같을 때 새를 키우는 사람의 폐암 odds는 새를 키우지 않는 사람의 약 `3.9배`이다.
- 기준집단 위험이 $P(LC\mid No\ Birds)=0.02$ 이므로, RR은
  $$
  RR=\frac{OR}{(1-p_0)+p_0\cdot OR}
  =\frac{3.90}{0.98+0.02\times 3.90}
  =\frac{3.90}{1.058}
  \approx 3.69
  $$
- 따라서 bird keeping 집단의 폐암 위험은 no-birds 집단보다 약 `3.69배`로 해석할 수 있다.

---


#### 문항 3

다음은 수업시간에 다룬 바와 같이 새를 키우는 사람과 폐암발생 간의 관계를 logistic regression 으로 모델링한 데이터이다. 다음 모델로부터 BKBird 가 LC 에 미치는 영향에 대한 predicted probability curve 를 그리시오. 단 그래프를 그릴 때 지나는 점을 네개 이상 구해서 그래프를 작성하시오. (15 점)

모형:

```r
glm(LC ~ FM + SS + BK + AG + YR + CD, data = bird, family = binomial)
```

회귀 결과 요약:

| Variable | Estimate | Std. Error | z value | Pr(>\|z\|) |
|---|---:|---:|---:|---:|
| (Intercept) | -1.93736 | 1.80425 | -1.074 | 0.282924 |
| FMFemale | 0.56127 | 0.53116 | 1.057 | 0.290653 |
| SSHigh | 0.10545 | 0.46885 | 0.225 | 0.822050 |
| BKBird | 1.36259 | 0.41128 | 3.313 | 0.000923 |
| AG | -0.03976 | 0.03548 | -1.120 | 0.262503 |
| YR | 0.07287 | 0.02649 | 2.751 | 0.005940 |
| CD | 0.02602 | 0.02552 | 1.019 | 0.308055 |

추가 정보:

- Null deviance: `187.14` on `146` degrees of freedom
- Residual deviance: `154.20` on `140` degrees of freedom
- AIC: `168.2`

변수 설명:

- `LC`: Whether subject has lung cancer
- `FM`: Sex of subject
- `SS`: Socioeconomic status
- `BK`: Indicator for birdkeeping
- `AG`: Age of subject (years)
- `YR`: Years of smoking prior to diagnosis or examination
- `CD`: Average rate of smoking (cigarettes per day)

---

#### 해설

- BK 효과만 보기 위해 다른 변수들을 0으로 고정하면 선형예측식은
  $$
  \eta=-1.93736+1.36259\cdot BK
  $$
  이다. 여기서 $BK=0$은 새를 키우지 않음, $BK=1$은 새를 키움이다.
- 확률은
  $$
  p=\frac{e^\eta}{1+e^\eta}
  $$
  로 계산한다.
- 대표적인 점들을 계산하면
  - $BK=0$: $\eta=-1.93736$, $p\approx 0.126$
  - $BK=0.25$: $\eta=-1.59671$, $p\approx 0.168$
  - $BK=0.50$: $\eta=-1.25607$, $p\approx 0.222$
  - $BK=0.75$: $\eta=-0.91542$, $p\approx 0.286$
  - $BK=1.00$: $\eta=-0.57477$, $p\approx 0.360$
- 이 점들을 찍으면 BK가 증가할수록 폐암 발생 예측확률이 상승하는 logistic curve를 그릴 수 있다.
- 실제 문항에서는 BK가 이진변수이므로 핵심은 `BK=0`과 `BK=1`의 예측확률 차이를 보여 주는 것이고, 중간값 점들은 곡선 형태를 그리기 위한 보조점으로 이해하면 된다.


## 15. PCA, 머신러닝, 모델 평가

- 이 섹션은 전통적 통계검정보다 데이터 분석 도구의 해석 능력을 묻는다. PCA plot 읽기, scaling의 필요성, supervised vs unsupervised learning, kMeans, decision tree, cross validation, overfitting이 주된 소재다.
- 좋은 PCA 문항은 축의 분산 설명력, 변수 간 유사성과 반대 방향, correlation circle에서의 거리와 각도의 의미를 직접 해석하게 한다.
- 머신러닝 문항은 특정 알고리즘 정의만 외우게 하기보다, 어떤 문제가 supervised이고 어떤 문제가 unsupervised인지, 모델을 어떻게 평가하고 과적합을 어떻게 피할지 설명하게 해야 한다.
- 최근 기출은 통계모델과 머신러닝을 따로 떼기보다, logistic regression을 supervised example로 드는 식으로 연결해 묻는 경향이 있다.
- 따라서 출제에서는 용어 비교형과 그림 해석형을 함께 섞어, 계산 대신 분석적 설명 능력을 보게 하는 편이 적절하다.
- PCA 해석 문항은 `같은 방향`, `반대 방향`, `원점에서의 거리`, `설명분산 비율`을 모두 읽게 해야 한다. 단순히 이름만 맞히는 문항은 변별력이 낮다.
- supervised와 unsupervised 비교형은 알고리즘 이름 나열보다 `정답 라벨이 있는가`, `무엇을 예측하거나 찾는가`, `평가 방식이 어떻게 다른가`를 쓰게 해야 한다.
- overfitting, cross validation, scaling은 서로 연결해 내는 편이 좋다. 모델을 잘 맞추는 것과 일반화 성능이 좋은 것은 다르다는 점이 이 섹션의 핵심이다.
- 채점은 `그림 해석 정확도`, `알고리즘 분류`, `평가 기준`, `과적합 방지 논리`를 따로 보는 구성이 적절하다.

### 실제 문항

---


#### 문항 1

Supervised machine learning 과 unsupervised machine learning 의 차이점을 설명하고 각각의 예(e.g. logistic regression)를 2 개 이상 들어보세요 (5 점)

---

#### 해설

- supervised learning 은 입력과 함께 정답(label)이 주어져 있어, 그 정답을 잘 예측하는 규칙을 학습하는 방식이다.
- 반면 unsupervised learning 은 정답이 주어지지 않은 상태에서 자료의 구조, 군집, 축소된 표현 등을 찾는 방식이다.
- 예를 들어 회귀와 분류는 supervised learning 이고, PCA 와 k-means 는 unsupervised learning 이다.
- 따라서 두 접근의 가장 큰 차이는 `예측해야 할 정답이 있느냐 없느냐`라고 설명할 수 있다.

---


#### 문항 2

Multivariate linear model 과 logistic linear model 을 평가하는 방법에 대해서 각각 서술하세요. (5 점)

---

#### 해설

- 모델 평가는 문제 유형에 따라 기준이 달라진다.
- 회귀문제에서는 예측값과 실제값의 차이를 보는 RMSE, MAE, 또는 설명력을 보는 $R^2$ 같은 지표가 중요하다.
- 분류문제에서는 accuracy 뿐 아니라 sensitivity, specificity, precision, ROC/AUC, confusion matrix 같은 지표가 중요하다.
- 따라서 서로 다른 모델을 비교할 때는 `무엇을 예측하는 문제인지`, `어떤 오류가 더 치명적인지`에 맞는 평가 기준을 선택해야 한다.

---


#### 문항 3

다음은 위스키에 대해 향 12 가지를 사람들에게 물어본 평가 결과를 PCA 분석한 결과이다. 설문은 대상 86 종의 위스키에 대해서 특정 향이 “없다” (0 점) 부터 “뚜렷하다” (4 점) 까지 평가한 결과를 바탕으로 한다. 이 분석에 대하여 다음에 대하여 답하세요 (5 점)

[image: PCA variable factor map on a correlation circle with aroma vectors including Honey, Winey, Nutty, Malty, Fruity, Sweetness, Floral, Spicy, Body, Smoky, Tobacco, and Medicinal; axes are Dim 1 (26.98%) and Dim 2 (15.94%)]

1. 위와 같은 그림의 이름은 무엇인가?
2. 위스키에서 ‘바디감’ (body)과 가장 유사한 향은 무엇인가?
3. ‘꿀’(Honey)향과 ‘꽃’(Floral)향은 어떠한 관계인가?
4. Dim 1 (26.98%), Dim 2 (15.94%)는 무엇을 나타내는가?

---

#### 해설

- 1) 이 그림의 이름은 PCA의 `variable factor map` 또는 `correlation circle` 이다. 변수들이 각 주성분 축에 어떻게 적재되는지 보여 주는 그림이다.
- 2) `Body`와 가장 유사한 향은 그림에서 가장 가까운 방향에 놓인 `Smoky`로 읽는 것이 적절하다. 두 벡터 방향이 비슷하면 함께 커지는 경향이 있다는 뜻이다.
- 3) `Honey`와 `Floral`은 거의 같은 방향에 있으므로 서로 `양의 상관` 관계에 있다고 해석한다. 한 향 점수가 높을수록 다른 향 점수도 함께 높아질 가능성이 크다.
- 4) `Dim 1 (26.98%)`, `Dim 2 (15.94%)`는 각각 첫 번째와 두 번째 주성분이 전체 변동 중 얼마나 설명하는지를 나타낸다.
- 따라서 이 두 축을 합치면
  $$26.98\%+15.94\%=42.92\%$$
  로, 그림이 전체 향 변동의 약 `42.92%`를 설명한다고 볼 수 있다.
- 이 그림에서 원점에서 멀리 있는 변수일수록 앞의 두 주성분에 의해 잘 설명되고, 서로 이루는 각이 작을수록 양의 상관, 180도에 가까울수록 음의 상관으로 해석한다.


## 16. 연구설계, randomization, causality

- 이 영역은 통계기법을 계산하기 전 단계에서 어떤 결론이 가능한지를 판단하는 축이다. experiment와 observational study의 차이, random sampling과 random assignment의 차이, blocking과 causality가 핵심이다.
- 좋은 문항은 용어 정의만 묻지 않고, 왜 관찰연구에서 인과를 단정할 수 없는지, random assignment가 왜 교란을 줄이는지, blocking이 분산을 줄이는 이유가 무엇인지를 사례 속에서 설명하게 해야 한다.
- 학생들은 종종 random sampling과 random assignment를 같은 것으로 혼동한다. 이 둘을 비교시키는 문항은 매우 효과적이다.
- 또한 within-subject / between-subject 설계와 연결해 반복측정이 무엇을 얻고 무엇을 잃는지도 설명하게 하면 설계 이해를 넓게 볼 수 있다.
- 이 영역은 계산이 거의 없더라도 시험 전체의 수준을 좌우한다. 연구설계의 논리를 이해하지 못하면 이후 검정 선택도 흔들리기 때문이다.
- 출제는 가능하면 결과 해석의 한계를 묻는 방향으로 가는 것이 좋다. `관련성은 말할 수 있지만 인과는 말할 수 없다` 같은 문장을 스스로 써 보게 해야 설계 감각이 드러난다.
- random sampling과 random assignment는 외적 타당도와 내적 타당도를 연결해 설명하게 하면 훨씬 좋은 답안이 나온다. 두 용어를 단순 번역 수준으로 쓰게 하면 변별력이 낮다.
- blocking과 repeated measure는 오차를 줄인다는 공통점이 있지만 설계 논리가 다르다. 이런 연결 비교를 통해 설계 이해를 넓게 점검할 수 있다.
- 채점은 `정의`, `가능한 결론의 범위`, `교란 통제 논리`, `설계 선택의 장단점`으로 나눠 보는 것이 적절하다.

### 실제 문항

---


#### 문항 1

Observational study 와 experiment 의 차이점을 설명하고 시행 시 주의할 점에 대하여 설명하시오 (5 점)

---

#### 해설

- observational study 는 연구자가 처치를 부여하지 않고 자연스럽게 발생한 자료를 관찰하는 연구다.
- experiment 는 연구자가 처치나 조건을 직접 할당하고 그 결과를 비교하는 연구다. 따라서 교란요인을 더 잘 통제할 수 있어 인과 추론에 더 유리하다.
- observational study 에서는 변수들 사이 관련성은 말할 수 있지만, 숨은 교란이 있을 수 있으므로 인과를 직접 단정하기 어렵다.
- 또한 random sampling 은 모집단 일반화와 관련이 깊고, random assignment 는 처치 비교의 공정성과 인과 추론과 더 직접적으로 연결된다는 점도 함께 써 주는 것이 좋다.


## 17. 개념 비교, 용어 서술, 참/거짓 종합형

- 실제 기출에서는 계산형 문항과 별도로, 개념 정의를 짧게 쓰게 하거나 비슷한 개념 둘을 구분하게 하거나 참/거짓 판단과 이유를 함께 요구하는 문항이 매우 자주 출제된다. 이 섹션의 목적은 공식을 외웠는지보다 `개념 경계`, `적용 조건`, `대표 오개념`을 드러내는 데 있다.
- 출제는 기본 용어 정의, 혼동하기 쉬운 개념 비교, 참/거짓 판단과 이유 서술을 함께 포함할 때 이해의 깊이를 안정적으로 구분할 수 있다.
- 용어 서술형은 정의만 적는 문항으로 끝내지 말고, `무엇을 뜻하는지`, `언제 등장하는지`, `왜 필요한지` 중 적어도 두 요소를 포함하게 해야 한다. 예를 들어 p-value, Bayes' Theorem, repeated measure, sphericity, collinearity는 단어 뜻만 쓰면 부분이해와 암기를 구분하기 어렵다.
- 비교형은 두 개념의 공통점보다 `무엇이 다르고 그래서 언제 어느 쪽을 선택하는가`를 쓰게 해야 한다. 단순 정의 나열보다 자료 구조, 가정, 해석 대상, 실험설계 차이를 포함하도록 유도하는 편이 채점과 변별에 유리하다.
- 참/거짓형은 짧지만 가장 쉽게 오개념이 드러나는 형식이다. 다만 정답 표시만으로는 실력을 가리기 어렵기 때문에, 이유를 한두 문장으로 반드시 붙이게 하고, 필요하면 반례나 올바른 문장을 다시 쓰게 하는 것이 좋다.
- 채점은 `정의의 정확성`, `적용 맥락 제시`, `혼동 개념과의 구분`, `오개념 수정 능력`을 분리해서 보는 것이 좋다. 같은 정답이라도 이유가 빈약하면 낮게, 용어는 다소 짧아도 핵심 조건과 해석을 정확히 짚으면 높게 평가하는 구성이 적절하다.
- 문제은행형 운영에서는 시험지 원문 묶음을 그대로 유지하기보다, 의미가 같은 항목은 통합하고 너무 운영성 성격이 강한 문항은 제거하는 편이 좋다. 현재 구성은 그 원칙에 맞춰 중복을 정리한 결과다.

### 문제 은행

#### 용어·서술형

1. (통계적 의미의) Independence 를 설명하시오.
   - 해설: Independence 는 한 사건이나 변수의 정보가 다른 사건이나 변수의 확률분포를 바꾸지 않는 상태다. 사건 기준으로는 $P(A \mid B)=P(A)$, 변수 기준으로는 결합분포가 주변분포의 곱으로 분해된다. 따라서 독립성은 `서로 관련이 전혀 없다`는 일상적 표현과 비슷해 보이지만, 통계에서는 매우 구체적인 확률 조건으로 정의된다는 점을 함께 써야 한다.
2. Squared Deviates 를 설명하시오.
   - 해설: Squared Deviates 는 각 관측치가 평균에서 얼마나 떨어졌는지를 제곱한 값 $(x_i-\bar x)^2$ 또는 $(x_i-\mu)^2$ 이다. 분산, 표준편차, ANOVA의 제곱합 계산은 모두 이 값을 바탕으로 한다. 제곱을 하는 이유는 음수와 양수 편차를 모두 양수로 바꾸고, 큰 편차에 더 큰 가중치를 주기 위해서라고 설명하면 더 완전하다.
3. Bimodal 을 설명하시오.
   - 해설: Bimodal 은 분포에 봉우리가 두 개 있는 상태다. 이런 분포는 서로 다른 두 하위집단이 섞여 있거나, 하나의 중심으로 자료를 설명하기 어렵다는 신호일 수 있다. 따라서 bimodal 자료를 단순 평균 하나로 요약하는 것은 부적절할 수 있다는 점까지 써 주는 것이 좋다.
4. Box plot 의 구성요소와 whisker 의 의미를 설명하시오.
   - 해설: Box plot 은 최소값, 제1사분위수, 중앙값, 제3사분위수, 최대값을 바탕으로 분포를 시각화하는 그림이다. box 는 IQR 범위를 나타내고, 중앙선은 median, whisker 는 보통 outlier 를 제외한 바깥 범위를 나타낸다. 따라서 box plot 은 중심, 퍼짐, 왜도, 이상치 존재를 한 번에 파악할 수 있는 요약 그래프라고 설명할 수 있다.
5. IQR 과 그 robustness 를 설명하시오.
   - 해설: IQR 은 $Q_3-Q_1$ 로 정의되며, 자료의 중간 50%가 얼마나 퍼져 있는지를 나타낸다. 평균에서 먼 극단값의 영향을 상대적으로 적게 받기 때문에 robust 한 퍼짐의 척도로 자주 사용된다. 특히 right skew 분포나 outlier 가 있는 자료에서는 SD보다 IQR이 더 적절한 경우가 많다.
6. Bernoulli distribution 을 설명하시오.
   - 해설: Bernoulli distribution 은 결과가 성공과 실패 두 값만 가지는 가장 기본적인 확률분포다. 보통 성공을 1, 실패를 0으로 두고 성공확률을 $p$로 표현한다. 이 분포는 binomial distribution 이나 geometric distribution 같은 더 큰 모형의 기본 단위라는 점도 함께 언급할 수 있다.
7. Binomial distribution(이항분포)을 설명하시오.
   - 해설: Binomial distribution 은 성공확률이 같은 독립 Bernoulli 시행을 $n$번 반복했을 때 성공 횟수를 다루는 분포다. 평균은 $np$, 분산은 $np(1-p)$이다. 따라서 이항분포 문제에서는 `성공 횟수`를 묻는지, `첫 성공까지 시행 수`를 묻는지부터 구분하는 것이 매우 중요하다.
8. Geometric distribution 을 설명하고 평균과 분산을 쓰시오.
   - 해설: Geometric distribution 은 첫 성공이 나올 때까지 시행 횟수를 다루는 분포다. 평균은 $1/p$, 분산은 $(1-p)/p^2$ 이다. 이 분포는 `몇 번 시도해야 처음 성공하나`를 다루므로, 성공 횟수를 세는 이항분포와 목적이 다르다는 점까지 써 주어야 한다.
9. Central Limit Theorem 을 설명하시오.
   - 해설: Central Limit Theorem 은 모집단 분포가 정규분포가 아니어도 표본 크기가 충분히 크면 표본평균의 분포가 평균 $\mu$, 분산 $\sigma^2/n$ 인 정규분포에 가까워진다는 정리다. 여기서 중요한 것은 원자료가 아니라 `표본평균의 분포`가 정규에 가까워진다는 점이다. 이 정리 덕분에 평균에 대한 신뢰구간과 가설검정을 폭넓게 수행할 수 있다.
10. Significance probability (p-value) 를 설명하시오.
   - 해설: p-value 는 귀무가설이 참이라고 가정했을 때, 지금 관측된 결과와 같거나 더 극단적인 결과가 나올 확률이다. 따라서 p-value 가 작다는 것은 현재 자료가 귀무가설과 잘 맞지 않는다는 뜻이지, 귀무가설이 참일 확률이 작다는 뜻은 아니다. 이 구분을 명확히 쓰는 것이 서술형 답안의 핵심이다.
11. Bayes' Theorem 을 설명하시오.
   - 해설: Bayes' Theorem 은 사전확률과 조건부확률을 이용해 사후확률을 갱신하는 공식이다. 식은 $P(A \mid B)=\dfrac{P(B \mid A)P(A)}{P(B)}$ 이다. 이 정리는 진단검사, 기계학습, 불확실성 갱신처럼 `새로운 정보를 보고 믿음을 업데이트하는 상황`에서 중요하다고 설명하면 좋다.
12. One-way ANOVA 의 가정을 설명하시오.
   - 해설: One-way ANOVA 의 가정은 관측치의 독립성, 각 집단의 정규성, 집단 간 등분산성이다. 독립성은 자료 수집 방식과 연결되고, 정규성과 등분산성은 F 통계량의 해석 타당성과 연결된다. 따라서 단순히 가정 이름만 나열하지 말고, 가정이 깨지면 검정 결과가 왜곡될 수 있다는 점까지 쓰는 것이 좋다.
13. One-way ANOVA 의 귀무가설과 대립가설을 설명하시오.
   - 해설: One-way ANOVA 의 귀무가설은 모든 집단 평균이 같다는 것이고, 대립가설은 적어도 하나의 집단 평균이 다르다는 것이다. 즉, ANOVA 는 `모든 평균이 같은가`를 한 번에 검정하는 절차이지, 어떤 두 집단이 다른지를 직접 알려 주는 절차는 아니다. 그래서 유의하면 보통 사후분석이 뒤따른다.
14. ANOVA 에서 MS(mean square) 를 설명하시오.
   - 해설: MS 는 mean square 로, 해당 SS를 그에 대응하는 자유도로 나눈 값이다. 분산 추정량처럼 해석되며, ANOVA에서는 집단간 평균제곱과 집단내 평균제곱의 비율로 F 통계량을 계산한다. 따라서 MS 는 단순 산술평균이 아니라, 제곱합을 자유도로 조정한 변동의 크기라고 설명해야 정확하다.
15. Repeated measure 를 설명하시오.
   - 해설: Repeated measure 는 같은 참가자에게 여러 조건을 반복 측정하는 설계다. 이 설계의 장점은 각 개인이 자신의 통제집단 역할을 하므로 개인차를 별도 요인으로 분리할 수 있다는 데 있다. 따라서 독립집단 설계보다 error term 을 줄여 더 민감한 비교를 가능하게 하는 경우가 많다.
16. Mann-Whitney U test (Wilcoxon rank sum test) 를 설명하시오.
   - 해설: Mann-Whitney U test 는 두 독립집단의 분포 위치 차이를 순위를 이용해 비교하는 비모수 검정이다. 정규성 가정을 강하게 두기 어려운 경우나 서열척도 자료에서 t-test 대신 사용할 수 있다. 다만 평균 자체를 직접 비교한다기보다, 두 집단의 순위 분포 차이를 본다는 점을 함께 적는 것이 좋다.
17. Wilcoxon signed rank test 를 설명하시오.
   - 해설: Wilcoxon signed rank test 는 대응표본이나 paired 자료에서 차이값의 부호와 크기를 순위화하여 검정하는 비모수 방법이다. 즉, 같은 사람의 전후 비교처럼 짝지어진 자료에 적합하다. Mann-Whitney 와 달리 독립집단이 아니라 대응 구조를 전제로 한다는 점을 분명히 해야 한다.
18. Kruskal-Wallis test 를 설명하시오.
   - 해설: Kruskal-Wallis test 는 세 집단 이상 독립집단의 분포 차이를 순위 기반으로 검정하는 비모수 방법이다. One-way ANOVA 의 비모수 대안으로 볼 수 있다. 정규성 가정이 약하거나 자료가 서열척도일 때 유용하지만, 유의하더라도 어느 집단이 다른지는 별도 post hoc 가 필요하다.
19. Friedman test 와 적용 가능한 데이터 유형을 설명하시오.
   - 해설: Friedman test 는 repeated measure 나 block 구조에서 세 조건 이상을 비교하는 비모수 검정이다. 즉, 독립집단용인 Kruskal-Wallis 와 달리 같은 대상이 여러 조건을 경험한 자료에 쓰인다. 따라서 대응 구조를 가진 서열자료 분석에서 매우 중요한 방법이다.
20. Bonferroni correction 을 설명하시오.
   - 해설: Bonferroni correction 은 다중비교에서 가족별 제1종 오류를 통제하기 위해 유의수준 $\alpha$ 를 비교 횟수 $m$ 으로 나누는 방법이다. 계산은 단순하지만 상당히 보수적이라는 특징이 있다. 즉, 거짓 양성은 줄이지만 검정력이 떨어질 수 있다는 점까지 같이 적으면 더 좋다.
21. Pooled variance 를 설명하시오.
   - 해설: Pooled variance 는 등분산 가정하에서 여러 집단의 분산 정보를 합쳐 공통 분산을 추정한 값이다. two-sample t-test 에서 두 집단 분산이 같다고 볼 때 표준오차를 계산하는 데 자주 사용된다. 따라서 pooled variance 는 `각 집단 분산의 단순 평균`이 아니라, 자유도를 반영해 결합한 분산 추정량이라는 점이 중요하다.
22. Logistic regression 을 설명하시오.
   - 해설: Logistic regression 은 종속변수가 이진형일 때 사건 발생 확률의 log-odds 를 explanatory variable 로 설명하는 회귀모형이다. 선형회귀처럼 예측변수의 선형결합을 쓰지만, 결과는 0과 1 사이 확률로 해석된다. 계수는 확률 자체가 아니라 log-odds 나 odds ratio 관점에서 읽어야 한다는 점을 함께 써야 한다.
23. ROC 를 설명하시오.
   - 해설: ROC 는 분류기의 threshold 를 바꿀 때 sensitivity 와 1-specificity 의 관계를 그린 곡선이다. AUC 는 그 곡선 아래 넓이로, 분류기가 전체적으로 얼마나 잘 구분하는지를 요약한다. 따라서 accuracy 하나로는 놓치기 쉬운 threshold 전반의 분류 성능을 평가할 수 있다는 점이 중요하다.
24. Linear regression 을 수행하기 위해 데이터가 만족해야 하는 조건을 설명하시오.
   - 해설: Linear regression 에서는 선형성, 오차의 독립성, 등분산성, 잔차 정규성, 심한 영향점의 부재를 점검해야 한다. 이 가정들이 크게 깨지면 회귀계수, 표준오차, 신뢰구간, 가설검정 결과가 왜곡될 수 있다. 따라서 residual plot, QQ plot, leverage diagnostics 같은 도구로 함께 확인하는 것이 일반적이다.
25. Collinearity 를 설명하시오.
   - 해설: Collinearity 는 explanatory variable 들이 강하게 선형관계를 가져 회귀계수 추정이 불안정해지는 현상이다. 이 경우 계수 부호가 흔들리거나, 표준오차가 커져 유의성이 약하게 보일 수 있다. 따라서 단순 상관뿐 아니라 VIF 같은 진단지표로 확인하는 경우가 많다.
26. Adjusted $R^2$ 를 설명하시오.
   - 해설: Adjusted $R^2$ 는 설명변수 수를 고려해 보정한 결정계수다. 일반 $R^2$ 는 변수를 추가하면 거의 항상 커지지만, adjusted $R^2$ 는 불필요한 변수를 넣으면 오히려 감소할 수 있다. 그래서 여러 회귀모형을 비교할 때 더 의미 있는 지표가 될 수 있다.
27. Goodness of fit test 를 설명하시오.
   - 해설: Goodness of fit test 는 관측된 분포가 기대한 이론분포나 모형과 잘 맞는지 검정하는 절차다. 예를 들어 범주형 자료에서 기대도수와 실제 관측도수를 비교해, 차이가 우연 수준인지 판단한다. 따라서 이 검정은 두 변수의 관련성을 보는 independence test 와는 목적이 다르다.
28. Causality 를 설명하시오.
   - 해설: Causality 는 한 변수가 다른 변수의 변화를 실제로 유발하는 관계를 뜻한다. 단순 상관은 두 변수가 함께 변한다는 사실만 말해 줄 뿐, 인과를 보장하지 않는다. 인과를 주장하려면 보통 실험설계, 교란 통제, 시간 순서 같은 추가 근거가 필요하다.
29. Blocking variable 을 설명하시오.
   - 해설: Blocking variable 은 관심 없는 변동원을 통제하기 위해 실험 설계에 포함하는 요인이다. 서로 비슷한 단위끼리 묶은 뒤 그 안에서 비교하면 오차를 줄이고 검정력을 높일 수 있다. 따라서 block 은 연구의 주효과 자체보다는 `불필요한 변동을 줄이는 장치`라고 설명하는 것이 좋다.
30. 구형성(Sphericity)을 설명하시오.
   - 해설: 구형성(Sphericity)은 repeated measure 조건 간 차이점수들의 분산이 서로 같다는 가정이다. 이 가정은 repeated measure ANOVA 의 F 검정 자유도 해석과 직접 연결된다. 따라서 구형성이 크게 위배되면 보정 없이 결과를 읽는 것은 위험하다.
31. Greenhouse-Geisser correction 을 설명하시오.
   - 해설: Greenhouse-Geisser correction 은 repeated measure ANOVA 에서 구형성이 위배될 때 자유도를 줄여 F 검정을 보수적으로 보정하는 방법이다. 즉, p-value 가 지나치게 작아지는 문제를 완화하는 역할을 한다. repeated design 에서 자주 등장하는 표준 보정법이라는 점도 함께 써 주면 좋다.
32. Interaction in two-way ANOVA 를 설명하시오.
   - 해설: Interaction in two-way ANOVA 는 한 요인의 효과가 다른 요인의 수준에 따라 달라지는 현상이다. 예를 들어 A 조건에서는 차이가 작지만 B 조건에서는 차이가 커진다면 interaction 이 있다고 본다. 따라서 interaction 이 유의하면 단순 main effect 만으로는 전체 결과를 충분히 설명할 수 없다.
33. Two-way RM ANOVA 의 post hoc test 를 어떻게 수행하는지 설명하시오.
   - 해설: Two-way RM ANOVA 의 post hoc test 는 interaction 또는 main effect 가 유의할 때 simple effects 나 pairwise comparisons 를 수행하고 다중비교 보정을 적용하는 방식으로 한다. 즉, 무조건 모든 쌍을 비교하는 것이 아니라 유의한 구조를 확인한 뒤 필요한 비교를 제한해서 수행해야 한다. paired 구조이므로 보통 paired comparison 형태가 자연스럽다.
34. Log transformation 을 설명하시오.
   - 해설: Log transformation 은 right skew 자료나 곱셈적 변동을 더 대칭적이고 안정적인 척도로 바꾸기 위해 로그를 취하는 변환이다. 특히 매우 큰 값이 일부 존재하는 자료에서 분포를 완화하고 등분산성이나 정규성 가정을 개선하는 데 도움이 된다. 다만 변환 뒤에는 해석이 원척도와 달라진다는 점도 유의해야 한다.
35. `subset()` in R 를 설명하시오.
   - 해설: `subset()` in R 는 조건에 맞는 행이나 일부 열을 선택해 데이터프레임의 일부를 추출하는 함수다. 예를 들어 특정 집단만 남기거나, 특정 변수들만 골라 분석할 때 쓸 수 있다. 즉, 분석 전에 자료를 필요한 형태로 정리하는 기본 도구라고 설명할 수 있다.
36. Backward elimination 을 위한 두 가지 방법을 설명하시오.
   - 해설: Backward elimination 은 보통 전체 모형에서 출발해 가장 덜 유의한 변수를 하나씩 제거하는 방법이다. 제거 기준으로는 p-value 를 쓸 수도 있고, AIC/BIC 같은 정보기준을 최소화하는 방향을 쓸 수도 있다. 따라서 핵심은 `큰 모형에서 시작해 점차 단순화한다`는 절차적 아이디어다.
37. Cross validation 을 설명하시오.
   - 해설: Cross validation 은 데이터를 학습용과 검증용으로 반복 분할하여 모델의 일반화 성능을 평가하는 절차다. 한 번의 train/test split 에 우연히 좌우되지 않도록 여러 번 반복한다는 점이 중요하다. 따라서 모델이 새 자료에서도 잘 작동하는지를 더 안정적으로 판단할 수 있다.
38. Overfitting 을 설명하시오.
   - 해설: Overfitting 은 학습자료의 잡음까지 과도하게 맞춰 새 자료에서 성능이 떨어지는 현상이다. 학습 데이터에서는 매우 잘 맞는 것처럼 보여도, 검증 데이터나 실제 새로운 데이터에서는 예측이 나빠질 수 있다. 따라서 모델 복잡도 조절과 cross validation 이 중요해진다.
39. Decision Tree 를 설명하시오.
   - 해설: Decision Tree 는 변수 분할 규칙을 반복 적용해 예측이나 분류를 수행하는 비선형 모형이다. 해석이 직관적이고 시각화가 쉽다는 장점이 있지만, 가지치기 없이 두면 overfitting 되기 쉽다. 그래서 보통 pruning 이나 ensemble 방법과 함께 언급된다.
40. PCA 에서 scaling 이 필요한 이유를 설명하시오.
   - 해설: PCA 에서 scaling 이 필요한 이유는 변수 단위와 분산 크기가 다르면 큰 스케일 변수만 주성분을 지배할 수 있기 때문이다. 즉, cm 단위 변수와 kg 단위 변수가 섞여 있으면 단위 차이만으로 분산이 크게 달라질 수 있다. scaling 은 각 변수를 비교 가능한 척도로 맞춰 PCA가 실제 구조를 반영하게 돕는다.
41. kMeans 알고리즘이 빠른 이유를 설명하시오.
   - 해설: kMeans 가 빠른 이유는 거리 계산과 중심 갱신을 단순 반복하는 구조이기 때문이다. 각 단계가 비교적 계산 효율적이고 구현도 간단해서 대용량 자료에도 널리 쓰인다. 다만 빠르다고 해서 항상 최적해를 보장하는 것은 아니며 초기 중심 선택의 영향도 받는다.
42. Extrapolation 의 위험성을 설명하시오.
   - 해설: Extrapolation 은 관측된 X 범위를 벗어난 구간에서 회귀식을 적용하는 것이다. 회귀선이 표본 범위 안에서는 잘 맞아도, 범위를 벗어나면 같은 관계가 유지된다는 보장이 없다. 따라서 extrapolation 결과는 특히 조심해서 해석해야 한다.
43. High leverage outlier 를 설명하시오.
   - 해설: High leverage outlier 는 X 방향으로 다른 점들과 멀리 떨어져 있어 회귀직선을 강하게 끌 수 있는 관측치다. 이런 점은 Y 값이 특별히 이상하지 않아도 회귀계수에 큰 영향을 줄 수 있다. 따라서 outlier 판단은 Y 방향만 보지 말고 X 공간에서의 위치도 함께 봐야 한다.
44. 모든 outlier 가 influential 한 것은 아님을 설명하시오.
   - 해설: 모든 outlier 가 influential 한 것은 아니다. 어떤 점은 Y 방향으로는 튀어 있어도 회귀선 전체를 크게 움직이지 않을 수 있다. 반대로 X 방향으로 멀리 있는 점은 값이 몇 개 안 되어도 회귀 결과를 강하게 바꿀 수 있으므로, outlier 와 influence 는 구분해서 봐야 한다.
45. Wilcoxon signed rank test 의 effect size 를 설명하시오.
   - 해설: Wilcoxon signed rank test 의 effect size 는 보통 $r=Z/\sqrt{N}$ 같은 형태로 요약한다. 이는 순위 기반 차이가 얼마나 강한지를 표준화해 보여 주는 값이다. 따라서 유의성 여부와 별도로 실제 차이의 크기를 설명하는 데 도움이 된다.
46. 이항분포의 정규 근사 조건을 설명하시오.
   - 해설: 이항분포의 정규 근사 조건은 보통 $np$ 와 $n(1-p)$ 가 모두 충분히 큰 경우다. 이는 성공과 실패가 한쪽에 너무 치우치지 않아야 정규분포 근사가 잘 맞는다는 뜻이다. 조건이 충족되지 않으면 exact binomial 방법을 쓰는 편이 더 적절하다.
#### 비교형

1. Response variable 과 Explanatory variable 을 비교 설명하시오.
   - 해설: Response variable 은 설명받는 결과 변수이고, Explanatory variable 은 그 결과를 설명하거나 예측하는 변수다. 즉, response 는 분석의 대상이고 explanatory 는 그 변화를 설명하는 원인 후보나 예측 변수다. 회귀식에서는 보통 Y가 response, X가 explanatory 로 놓인다.
2. Slope 와 Intercept 를 비교 설명하시오.
   - 해설: Slope 는 X가 1단위 증가할 때 Y가 평균적으로 얼마나 변하는지를 나타내는 계수다. Intercept 는 X=0일 때의 예측 Y값이다. 따라서 slope 는 변화율의 해석에, intercept 는 기준점의 해석에 해당하지만, intercept 는 맥락에 따라 실질적 의미가 약할 수도 있다.
3. 분산과 IQR 을 비교 설명하시오.
   - 해설: 분산은 평균을 중심으로 한 제곱거리의 평균이라 outlier 에 민감하다. IQR 은 중간 50% 범위를 보는 척도라 극단값 영향이 작다. 따라서 대칭적이고 이상치가 적은 분포에서는 분산/SD, 왜도나 outlier 가 있는 분포에서는 IQR 이 더 적절할 수 있다.
4. Random sampling 과 Random assignment 를 비교 설명하시오.
   - 해설: Random sampling 은 표본을 모집단에서 무작위로 뽑는 절차로, 결과를 더 넓은 모집단에 일반화하는 데 중요하다. Random assignment 는 실험 조건을 무작위로 배정하는 절차로, 교란을 줄여 인과 추론을 강화한다. 따라서 두 개념은 둘 다 `random` 이라는 말을 쓰지만 목적이 전혀 다르다.
5. Experiment 와 Observational study 를 비교 설명하시오.
   - 해설: Experiment 는 연구자가 처치를 직접 할당하고 그 결과를 비교하는 연구다. Observational study 는 처치를 할당하지 않고 자연스럽게 발생한 자료를 관찰한다. 따라서 experiment 는 인과 추론에 더 강하고, observational study 는 관련성 분석에 더 자주 쓰인다.
6. Type I Error 와 Type II Error 를 비교 설명하시오.
   - 해설: Type I Error 는 귀무가설이 참인데 기각하는 거짓 양성이고, Type II Error 는 귀무가설이 거짓인데 기각하지 못하는 거짓 음성이다. 전자는 `없는데 있다고 판단`, 후자는 `있는데 없다고 판단`으로 번역하면 더 쉽다. 검정 설계에서는 두 오류를 동시에 완전히 없앨 수 없다는 점도 중요하다.
7. 단측검정(One-tailed test)과 양측검정(Two-tailed test)을 비교 설명하시오.
   - 해설: 단측검정은 효과의 방향이 정해진 대립가설을 쓴다. 양측검정은 방향 없이 차이 존재 자체를 묻는다. 따라서 같은 자료라도 단측검정은 한 방향에 더 민감하지만, 방향을 잘못 정하면 중요한 차이를 놓칠 수 있다.
8. 신뢰구간과 가설검정을 비교 설명하시오.
   - 해설: 신뢰구간은 모수의 plausible range 를 제시하는 추정 방법이고, 가설검정은 특정 귀무가설을 기각할지 판단하는 절차다. 두 방법은 서로 다른 형식처럼 보이지만 같은 추론 논리를 공유한다. 예를 들어 신뢰구간에 귀무가설 값이 포함되지 않으면 보통 같은 수준의 가설검정에서도 기각된다.
9. t-test 와 paired t-test 를 비교 설명하시오.
   - 해설: t-test 는 두 독립집단 평균 비교에 쓰고, paired t-test 는 같은 대상의 전후 비교나 짝지어진 자료의 평균차 비교에 쓴다. paired t-test 는 차이값 하나의 평균을 검정한다고 이해하면 쉽다. 따라서 자료가 독립인지 대응인지 구분하는 것이 가장 중요하다.
10. t-test 와 ANOVA 를 비교 설명하시오.
   - 해설: t-test 는 두 집단 평균 비교, ANOVA 는 세 집단 이상 평균 비교에 적합하다. 그러나 두 집단만 있을 때 one-way ANOVA 와 t-test 는 본질적으로 같은 검정을 다른 형태로 표현한 것이다. 따라서 ANOVA 는 t-test 를 일반화한 방법이라고 볼 수 있다.
11. One-way ANOVA 와 Two-way ANOVA 를 비교 설명하시오.
   - 해설: One-way ANOVA 는 요인 하나의 평균 차이를 검정하고, Two-way ANOVA 는 요인 둘의 main effect 와 interaction 을 함께 본다. 따라서 two-way ANOVA 는 단순 평균 비교를 넘어서, 한 요인의 효과가 다른 요인의 수준에 따라 달라지는지까지 확인할 수 있다.
12. ANOVA 와 RM ANOVA 를 비교 설명하시오.
   - 해설: ANOVA 는 보통 독립집단 설계에서 집단 평균을 비교하고, RM ANOVA 는 같은 참가자를 여러 조건에서 반복 측정한 자료를 다룬다. RM ANOVA 는 subject variation 을 따로 떼어내기 때문에 더 정밀한 비교가 가능한 경우가 많다. 따라서 두 방법은 데이터 구조 자체가 다르다.
13. Between-subject 와 Within-subject 실험계획을 비교 설명하시오.
   - 해설: Between-subject 설계는 서로 다른 참가자가 각 조건에 배정된다. Within-subject 설계는 같은 참가자가 여러 조건을 모두 경험한다. 전자는 carryover effect 가 적지만 개인차가 크고, 후자는 개인차를 줄일 수 있지만 순서효과나 피로효과를 관리해야 한다.
14. Chi-Square test of Independence 와 Goodness of fit test 를 비교 설명하시오.
   - 해설: Chi-square test of Independence 는 두 범주형 변수의 관련성을 본다. Goodness of fit test 는 한 변수의 관측 분포가 기대 분포와 맞는지를 본다. 둘 다 chi-square 통계량을 쓸 수 있지만, 연구 질문과 기대도수 계산 구조가 다르다.
15. Tukey HSD 와 multiple t-tests 를 비교 설명하시오.
   - 해설: Tukey HSD 는 ANOVA 이후 여러 쌍비교를 하면서 family-wise error 를 통제하는 공식적인 사후검정이다. multiple t-tests 를 보정 없이 반복하면 제1종 오류가 누적된다. 따라서 집단 수가 많을수록 Tukey 같은 보정된 방법이 더 적절하다.
16. Wilcoxon test 와 t-test 의 가정 차이를 비교 설명하시오.
   - 해설: Wilcoxon test 는 정규성 가정이 약하거나 서열자료에 적합한 비모수 방법이다. t-test 는 평균 비교를 전제로 하며 연속형 자료와 더 강한 분포 가정을 둔다. 따라서 둘은 같은 질문을 다룰 수도 있지만, 자료 수준과 가정에 따라 선택 기준이 달라진다.
17. Odds ratio 와 Relative risk 를 비교 설명하시오.
   - 해설: Odds ratio 는 odds 의 비이고, Relative risk 는 확률의 비다. OR은 로지스틱 회귀에서 자연스럽게 나오지만, RR 보다 직관성이 떨어질 수 있다. 특히 사건이 흔할 때 OR이 RR보다 더 크게 보여 효과를 과장해 읽을 위험이 있다.
18. Sensitivity 와 Specificity 를 비교 설명하시오.
   - 해설: Sensitivity 는 실제 양성 중 양성으로 맞춘 비율이고, Specificity 는 실제 음성 중 음성으로 맞춘 비율이다. 하나는 양성 탐지 능력, 다른 하나는 음성 배제 능력을 뜻한다. 따라서 어떤 지표를 더 중시할지는 문제의 목적에 따라 달라진다.
19. 정규분포와 t 분포를 비교 설명하시오. 어떤 상황에서 각각을 사용하는지 서술하시오.
   - 해설: 정규분포는 모집단 분포 자체를 설명하거나, 모집단 표준편차를 아는 상황의 z 기반 추론에서 자주 등장한다. t 분포는 표본이 작고 모집단 표준편차를 모를 때 평균 추론에 쓰인다. 자유도가 커질수록 t 분포는 정규분포에 가까워진다.
20. Parametric method 와 Non-parametric method 를 비교 설명하시오. 어떤 자료와 가정에서 각각을 선택하는지 서술하시오.
   - 해설: Parametric method 는 모집단 분포나 모수 형태에 대한 가정을 사용하는 방법이다. Non-parametric method 는 그런 가정이 약하고, 순위나 부호 정보를 많이 사용한다. 따라서 자료가 가정을 잘 만족하면 parametric 방법이 효율적일 수 있고, 가정 위반이 크면 non-parametric 방법이 더 적절할 수 있다.
21. Mosaic plot 과 Stacked bar graph 를 비교 설명하시오.
   - 해설: Mosaic plot 은 각 셀의 빈도와 비율을 면적 형태로 표현해 범주형 변수 관계를 직관적으로 보여 준다. Stacked bar graph 는 범주별 구성비를 막대 누적으로 표현한다. 따라서 mosaic plot 이 더 직접적으로 셀 빈도 구조를 보여 주는 반면, stacked bar graph 는 범주별 비율 비교가 더 익숙할 수 있다.
22. High leverage point 와 Influential point 를 비교 설명하시오.
   - 해설: High leverage point 는 X 공간에서 멀리 떨어진 점이고, Influential point 는 회귀선 추정 결과를 크게 바꾸는 점이다. leverage 가 높다고 해서 반드시 influential 한 것은 아니다. 그러나 높은 leverage 를 가진 점은 모델을 크게 끌 가능성이 있으므로 특별히 주의해서 봐야 한다.
#### 참/거짓형

1. The chi-square statistic is always positive.
   - 해설: 참. chi-square 통계량은 제곱합 구조라 음수가 될 수 없다.
2. 자유도의 크기와 상관없이 chi-square distribution 은 항상 right skewed 이다.
   - 해설: 참. 자유도가 커져도 양의 방향 꼬리를 가진 분포라는 점은 유지된다.
3. 자유도가 커질수록 chi-square distribution 의 평균은 증가한다.
   - 해설: 참. chi-square 분포의 평균은 자유도와 같다.
4. 자유도가 커질수록 chi-square distribution 의 variability 는 감소한다.
   - 해설: 거짓. 분산은 $2df$ 이므로 자유도가 커질수록 절대적 variability 는 증가한다.
5. 자유도가 커질수록 chi-square distribution 의 모양은 더욱 더 skew 된다.
   - 해설: 거짓. 자유도가 커질수록 오히려 덜 skew 되고 대칭적인 모양에 가까워진다.
6. When finding the p-value of a chi-square test, we always shade the tail areas in both tails.
   - 해설: 거짓. chi-square 검정의 p-value 는 보통 오른쪽 꼬리만 본다.
7. 조건부 확률 $P(A \mid B)$ 는 A 와 B 가 독립이면 항상 $P(A)$ 와 같다.
   - 해설: 참. 독립이면 $P(A \mid B)=P(A)$ 이다.
8. 80%의 사람이 케익을 좋아하고 75%의 사람이 쿠키를 좋아하며, 둘 다 좋아하는 사람은 60%이다. 어떤 랜덤한 사람이 케익을 좋아할 때 이 사람이 쿠키도 좋아할 확률은 75%이다.
   - 해설: 참. $P(\text{쿠키} \mid \text{케익})=0.60/0.80=0.75$.
9. A correlation coefficient of -0.90 indicates a stronger linear relationship than a correlation coefficient of 0.5.
   - 해설: 참. 선형관계의 세기는 절댓값으로 보므로 $|-0.90| > |0.5|$ 이다.
10. 모집단에서 랜덤하게 샘플한 값은 항상 정규분포를 따른다.
   - 해설: 거짓. 랜덤 표본값 자체는 모집단 분포를 따르며, 그 모집단이 정규라는 보장은 없다.
11. 분포가 right skew 인 경우 median 의 값이 mean 보다 크다.
   - 해설: 거짓. right skew 에서는 보통 mean > median 이다.
12. two sample t-test 를 수행할 때 모집단의 분산이 같다고 항상 가정할 필요는 없다.
   - 해설: 참. Welch t-test 처럼 등분산을 가정하지 않는 방법도 있다.
13. Paired t-test 는 two sample t-test 를 수행할 수 있는 경우 항상 수행할 수 있다.
   - 해설: 거짓. paired t-test 는 대응 구조가 있어야만 가능하다.
14. One-way RM ANOVA 는 One-way ANOVA 보다 항상 유의한 결과를 보여준다.
   - 해설: 거짓. RM ANOVA 가 항상 더 유의한 것은 아니다.
15. If the null hypothesis that the means of four groups are all the same is rejected using one way ANOVA at a 5% significance level, the standardized variability between groups is higher than the standardized variability within groups.
   - 해설: 참. 귀무가설을 기각했다면 between-group variability 가 within-group variability 에 비해 충분히 크다는 뜻이다.
16. Post hoc 분석은 ANOVA 분석 이후 반드시 수행하여야 한다.
   - 해설: 거짓. ANOVA가 유의하지 않으면 post hoc 가 필요 없고, 연구 질문에 따라 꼭 모든 경우에 반드시 하는 것도 아니다.
17. In pairwise comparisons after a four-group one-way ANOVA, the appropriate $\alpha$ is 0.05 / 4.
   - 해설: 거짓. 네 집단 pairwise 비교는 6쌍이므로 단순 Bonferroni 라면 $0.05/6$ 이다.
18. Effect size 는 항상 0 과 1 사이의 값을 가진다.
   - 해설: 거짓. effect size 가 항상 0과 1 사이인 것은 아니다. 예를 들어 Cohen's d 는 1을 넘을 수 있다.
19. ANOVA 에서 effect size 가 1.0 에 가까이 갈수록 $SS_{BG}$ 는 $SS_{WG}$ 에 비해 작아진다.
   - 해설: 거짓. effect size 가 커질수록 보통 $SS_{BG}$ 가 $SS_{WG}$ 에 비해 커진다.
20. One-way ANOVA 는 multiple comparison 으로 대체 수행 가능하다.
   - 해설: 거짓. multiple comparison 을 그대로 one-way ANOVA 대체로 쓰면 제1종 오류 문제가 생긴다.
21. t-분포는 자유도가 커짐에 따라서 꼬리가 점점 두꺼워진다.
   - 해설: 거짓. 자유도가 커질수록 꼬리는 얇아지고 정규분포에 가까워진다.
22. 자유도가 커질수록 t distribution 의 모양은 더욱 더 skew 된다.
   - 해설: 거짓. 자유도가 커질수록 skew 가 커지는 것이 아니라 줄어든다.
23. 자유도가 커질수록 t distribution 의 평균은 증가한다.
   - 해설: 거짓. t 분포의 평균은 자유도 1 초과에서 0이다.
24. 비모수 검정은 해당하는 모수검정에 비해 항상 큰 p 값을 가진다.
   - 해설: 거짓. 비모수 검정이 항상 더 큰 p 값을 갖는 것은 아니다.
25. 이항분포의 정규근사는 항상 사용할 수 있다.
   - 해설: 거짓. $np$ 와 $n(1-p)$ 가 충분히 크지 않으면 정규근사가 부적절하다.
26. Two-way RM ANOVA 에서 구형성이 위배되면 비모수 방법을 사용해야 한다.
   - 해설: 거짓. 구형성 위배 시 Greenhouse-Geisser 같은 보정을 먼저 고려하며, 비모수로 반드시 바꿔야 하는 것은 아니다.
27. 오류의 추정 시 샘플의 크기는 모집단의 크기를 우선적으로 고려하여 정한다.
   - 해설: 거짓. 표본크기는 원하는 오차범위, 신뢰수준, 모집단 변동성 등이 핵심이며 모집단 크기만 우선하는 것은 아니다.
28. High leverage outlier 는 r 을 크게 만들 수 있다.
   - 해설: 참. X방향으로 멀리 떨어진 점은 상관계수와 회귀선을 크게 키우거나 줄일 수 있다.
29. 죄가 없는 사람을 범인으로 결정하는 오류는 Type I 오류이다.
   - 해설: 참. 무죄한 사람을 유죄라고 판단하는 것은 귀무가설이 참인데 기각한 Type I error 에 해당한다.
30. 비모수적 통계분석 방법은 모수를 순위로 바꾸어 시행하므로 모수적 방법보다 정확도가 떨어진다.
   - 해설: 거짓. 비모수 방법은 가정 위반 상황에서 오히려 더 적절할 수 있으며, 항상 정확도가 떨어진다고 할 수 없다.

---
