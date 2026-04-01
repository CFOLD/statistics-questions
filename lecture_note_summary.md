# 통계분석 강의노트 Part 1
## 기본 개념 & 확률

---

# 1. 변수와 데이터

## 변수의 종류

**수치형 (Numerical)**
- **연속형 (Continuous)**: 어떤 값도 가질 수 있음 (예: 키, 체중)
- **이산형 (Discrete)**: 특정 값만 가질 수 있음 (예: 자녀 수)

**범주형 (Categorical)**
- **명목 (Nominal)**: 순서가 없음 (예: 성별, 국적)
- **서열 (Ordinal)**: 순서가 있음 (예: Likert scale, 건강상태)

| 척도 | 특징 | 대표값 |
|------|------|--------|
| Nominal | 같음/다름만 의미 | Mode |
| Ordinal | 순서만 의미 | Median |
| Interval | 순서 + 간격 의미, 절대적 0 없음 | Mean |
| Ratio | 순서 + 간격 + 절대적 0 있음, 비율 비교 가능 | Mean |

## 변수 관계

- **설명변수 (Explanatory/Independent X)**: 다른 변수에 영향을 줄 것으로 추정되는 변수
- **반응변수 (Response/Dependent Y)**: 영향을 받을 것으로 추정되는 변수
- **주의**: "correlation ≠ causation"

---

# 2. 표본추출 (Sampling)

## 모집단 vs 표본

- **모집단 (Population)**: 연구 대상 전체
- **표본 (Sample)**: 모집단에서 선택된 일부
- **편향 (Bias)**:
  - 선택 편향 (selection bias)
  - 자기선택 편향 (self-selection bias)
  - 비응답률 (non-response rate)

## 관찰연구 vs 실험

| | 관찰연구 (Observational) | 실험 (Experiment) |
|---|------------------------|------------------|
| 인과추론 | 어려움 | 유리함 |
| 무작위 할당 | X | O |
| 목적 | 관계 파악 | 인과 검증 |

## 실험 설계 원칙

1. **통제 (Control)**: 대조군과 비교
2. **무작위화 (Randomize)**: 무작위 할당
3. **반복 (Replicate)**: 충분한 표본
4. **블로킹 (Block)**: 알려진 변수로 그룹화 후 무작위화

---

# 3. 데이터 요약

## 중심경향

- **평균 (Mean)**: $\bar{x} = \frac{\sum x_i}{n}$
- **중앙값 (Median)**: 50 번째 백분위수
- **최빈값 (Mode)**: 가장 많은 값

**예제: Mean/Median/Mode 계산**

데이터: {2, 4, 4, 4, 5, 7, 8}
- Mean: $\bar{x} = (2+4+4+4+5+7+8)/7 = 34/7 = 4.86$
- Median: 4 (정중앙 값)
- Mode: 4 (가장 많은 값)

## 분산 (Spread)

- **분산 (Variance)**: $s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$
- **표준편차 (SD)**: $s = \sqrt{s^2}$
- **IQR**: $Q_3 - Q_1$ (중간 50% 범위)

**예제: Variance/SD 계산**

데이터: {2, 4, 4, 4, 5, 7, 8}, $\bar{x} = 4.86$

| x | x - x̄ | (x - x̄)² |
|---|-------|----------|
| 2 | -2.86 | 8.18 |
| 4 | -0.86 | 0.74 |
| 4 | -0.86 | 0.74 |
| 4 | -0.86 | 0.74 |
| 5 | 0.14 | 0.02 |
| 7 | 2.14 | 4.58 |
| 8 | 3.14 | 9.86 |
| **Sum** | | **24.86** |

$$s^2 = \frac{24.86}{7-1} = 4.14$$
$$s = \sqrt{4.14} = 2.04$$

## 분포의 모양

- 단봉 (unimodal), 이중봉 (bimodal), 다중봉 (multimodal)
- 대칭 (symmetric), 우측왜도 (right skew), 좌측왜도 (left skew)
- 균일 (uniform)

## Robust 통계량

| | Robust | Not Robust |
|---|--------|------------|
| 중심 | Median | Mean |
| 분산 | IQR | SD |

- 왜도된 분포 → Median, IQR 사용
- 대칭 분포 → Mean, SD 사용

---

# 4. 확률 기초

## 이항분포 (Binomial Distribution)

n 번의 독립적인 베르누이 시행에서 정확히 k 번 성공할 확률:

$$P(k) = \binom{n}{k} p^k (1-p)^{n-k}$$

- 기대값: $\mu = np$
- 표준편차: $\sigma = \sqrt{np(1-p)}$

### 정규근사 조건

$$np \geq 10 \text{ and } n(1-p) \geq 10$$

충족시: $Bin(n, p) \approx N(np, np(1-p))$
- 평균: $np$
- 분산: $np(1-p)$
- 표준편차: $\sqrt{np(1-p)}$

**예제: 이항분포 확률 계산**

동전을 10 번 던졌을 때 정확히 7 번 앞면이 나올 확률:
- $n = 10, k = 7, p = 0.5$

$$P(7) = \binom{10}{7} (0.5)^7 (0.5)^3 = 120 \times 0.0078125 = 0.11719$$

**예제: 기대값과 표준편차**

질병 발생률 2%, 표본 500 명일 때:
- 기대 발병자: $\mu = np = 500 \times 0.02 = 10$ 명
- 표준편차: $\sigma = \sqrt{500 \times 0.02 \times 0.98} = 3.13$

### 기하분포 (Geometric Distribution)

iid 베르누이 시행에서 **첫 번째 성공까지의 시행 횟수**:

$$P(\text{success on } n^{th} \text{ trial}) = (1 - p)^{n-1} p$$

- 기대값: $E(X) = \frac{1}{p}$
- 분산: $Var(X) = \frac{1-p}{p^2}$

**예제: 주사위 6 이 처음 나올 때까지**

주사위를 던져 6 이 처음으로 6 번째 시행에서 나올 확률:
- 성공: 6 출현, $p = 1/6$
- $P(6 \text{ on } 6^{th} \text{ roll}) = (5/6)^5 \times (1/6) \approx 0.067$
- 기대 시행 횟수: $E(X) = 1/(1/6) = 6$

### 확률변수 (Random Variable)

- **정의**: 확률실험의 결과를 수치로 표현한 변수
- **이산형**: 유한개/가산개의 값 (Binomial, Geometric)
- **연속형**: 무한개의 값 (Normal, Uniform)

**예제: 기대값과 분산 계산**

주사위를 던져 나온 눈의 수를 확률변수 X 라고 함:

| X | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| P(X) | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 |

기대값:
$$E(X) = \sum x \cdot P(X=x) = 1\cdot\frac{1}{6} + 2\cdot\frac{1}{6} + 3\cdot\frac{1}{6} + 4\cdot\frac{1}{6} + 5\cdot\frac{1}{6} + 6\cdot\frac{1}{6} = 3.5$$

분산:
$$Var(X) = \sum (x - \mu)^2 \cdot P(X=x) = \frac{(1-3.5)^2 + (2-3.5)^2 + \cdots + (6-3.5)^2}{6} = \frac{17.5}{6} \approx 2.92$$

표준편차: $\sigma = \sqrt{2.92} \approx 1.71$

### 확률의 종류

| 개념 | 공식 | 설명 |
|------|------|------|
| **Marginal Probability** | $P(A)$ | 주변확률, 전체에서의 A 확률 |
| **Joint Probability** | $P(A \cap B)$ | 공동확률, A와 B가 동시에 일일 확률 |
| **Conditional Probability** | $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ | 조건부확률, B가 일어났을 때 A의 확률 |

**베이즈 정리 (Bayes' Theorem)**:
$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

**예제: 조건부 확률 계산**

100 명 중 남성이 60 명, 여성 40 명. 남성 중 30 명이 흡연자, 여성 중 10 명이 흡연자.

- $P(\text{Male}) = 60/100 = 0.6$
- $P(\text{Smoker} \cap \text{Male}) = 30/100 = 0.3$

남성이면 흡연자일 확률:
$$P(	ext{Smoker} \mid 	ext{Male}) = \frac{P(\text{Smoker} \cap \text{Male})}{P(\text{Male})} = \frac{0.3}{0.6} = 0.5$$

흡연자면 남성일 확률:
$$P(	ext{Male} \mid 	ext{Smoker}) = \frac{P(\text{Male} \cap \text{Smoker})}{P(\text{Smoker})} = \frac{0.3}{0.4} = 0.75$$

**예제: 유방암 검사 (Bayes 정리 적용)**

유방암 검사에서:
- 암 발생률: $P(\text{Cancer}) = 0.017$
- 민감도: $P(	ext{+} \mid 	ext{Cancer}) = 0.78$
- 거짓 양성: $P(	ext{+} \mid 	ext{No Cancer}) = 0.10$

검사가 양성일 때 실제 암일 확률:
$$P(	ext{Cancer} \mid 	ext{+}) = \frac{P(	ext{+} \mid 	ext{Cancer}) \times P(\text{Cancer})}{P(\text{+})}$$

$$P(\text{+}) = P(	ext{+} \mid 	ext{Cancer}) \times P(\text{Cancer}) + P(	ext{+} \mid 	ext{No Cancer}) \times P(\text{No Cancer})$$
$$= 0.01326 + 0.0983 = 0.11156 \approx 0.1116$$

$$P(	ext{Cancer} \mid 	ext{+}) = \frac{0.78 \times 0.017}{0.1116} \approx 0.12$$

→ 양성 판정을 받아도 암일 확률은 약 12% (대부분이 거짓 양성)

---

## 이상관측치 (Unusual Observations)

**경험적 기준**: 정규분포에 가까운 데이터에서 평균에서 2 표준편차 이상 떨어진 관측치를 unusual 로 간주 (일반적인 outlier 판정 기준은 아님):

$$\text{usual range} = \mu \pm 2\sigma$$

(참고: 실제 outlier 판정에는 1.5×IQR, standardized residual 등을 사용)

(참고: 2SD 는 약 95% 포함, 3SD 는 더 엄격한 기준)

---

# 5. 표본분포와 CLT

## 중심극한정리 (CLT)

모집단이 정규분포이면 표본평균도 정규분포, 그렇지 않으면 n 이 충분히 크면 근사적으로 정규분포:

$$\bar{x} \approx N\left(\mu, \frac{\sigma^2}{n}\right)$$

- 평균 (mean): $\mu$
- 분산 (variance): $\sigma^2/n$
- 표준오차 (SE) = $\sigma / \sqrt{n}$
- n 이 증가하면 SE 는 감소

**참고**: 모집단이 정규분포이면 등호 (=) 가 가능.

### 적용 조건

1. **독립성**: 무작위 추출, 10% 조건 (n < 모집단의 10%)
2. **표본크기**: n ≥ 30 (경험적 기준, 왜도/이상치가 심하면 더 큰 n 필요)

---

# 6. 신뢰구간 (Confidence Interval)

## 95% 신뢰구간

$$\text{estimate} \pm \text{critical value} \times SE$$

- σ를 알면: $z^*$ (95%: 1.96, 99%: 2.58)
- σ를 모르면: $t^*$ (df 에 따라 결정)

## 신뢰구간 해석

"95% 신뢰구간" = 여러번 표본추출 시 95% 의 구간이 모평균을 포함함

**예제: 신뢰구간 계산**

어떤 제품의 무게에 대해 n = 100 개 표본을 추출했을 때:
- 표본평균: $\bar{x} = 250$g
- 표준편차: $s = 20$g

95% 신뢰구간:
$$SE = \frac{s}{\sqrt{n}} = \frac{20}{\sqrt{100}} = 2$$

$$95\% CI = 250 \pm 1.96 \times 2 = 250 \pm 3.92 = (246.08, 253.92)$$

해석: "이 절차를 반복할 때, 만들어지는 구간의 95% 가 모평균을 포함한다. (모수 자체가 확률변수가 아님)"

**참고**: z* = 1.96 사용은 σ를 알 때 원칙. σ를 모르면 t*를 써야 하지만, n = 100 이면 z 근사가 매우 좋음.

## 신뢰구간 조건

1. **독립성**: 무작위 추출, 10% 조건
2. **표본크기/왜도**: n ≥ 30, 극단적 왜도 없음

---

# 7. 가설검정 (Hypothesis Testing)

## 검정 프레임워크

1. **가설 설정**: $H_0$ (귀무), $H_A$ (대립)
2. **조건 확인**: 독립성, 정규성/표본크기
3. **검정통계량 계산**
4. **p-value 계산**: $P(\text{관측}  \mid  H_0 \text{ true})$
5. **결론**: p-value < α → $H_0$ 기각

## p-value

- 귀무가설이 참일 때, 관측된 값과 같거나 더 극단적인 값이 나올 확률
- **주의**: p-value는 "귀무가설이 참일 확률"이 아님
- p-value < 0.05 → $H_0$ 기각 (유의성)
- p-value > 0.05 → $H_0$ 기각하지 않음

## Type 1 & 2 Error

| | $H_0$ 참 | $H_A$ 참 |
|---|----------|----------|
| $H_0$ 기각하지 않음 | ✓ | Type 2 Error |
| $H_0$ 기각 | Type 1 Error | ✓ |

- **Type 1 Error**: $H_0$ 가 참인데 기각 (거짓 양성)
- **Type 2 Error**: $H_A$ 가 참인데 $H_0$ 기각하지 않음 (거짓 음성)
- $P(\text{Type 1}  \mid  H_0 \text{ true}) = \alpha$ (유의수준)

---

# 정규화 (Standardization) 와 정규분포

## Z-score (Standardized Score)

- **정의**: 관측치가 평균으로부터 몇 표준편차만큼 떨어져 있는지를 나타내는 값
- **공식**: $Z = \frac{x - \mu}{\sigma}$ (개별 관측치) 또는 $Z = \frac{\bar{x} - \mu}{SE}$ (표본평균)
- **용도**:
  - 다른 단위/규모의 데이터를 비교 가능하게 함
  - 이상치 탐지 (|Z| > 3 은 극단적 값으로 간주)
  - 정규분포에서 백분위수 계산 가능

**예제: Z-score 계산**

어떤 시험의 평균이 70 점, 표준편차가 10 점일 때:

1. 85 점의 Z-score: $Z = \frac{85 - 70}{10} = 1.5$
   → 평균보다 1.5 표준편차 높음

2. Z = -2 인 학생의 점수: $x = 70 + (-2 \times 10) = 50$ 점

3. 95 번째 백분위수 (95% 이하): Z = 1.645 → 점수 = $70 + 1.645 \times 10 = 86.45$ 점
   (참고: 중앙 95% 구간은 ±1.96)

## 정규분포 (Normal Distribution)

- **표기**: $N(\mu, \sigma^2)$ (두 번째 인자는 **분산**)
  - $\mu$: 평균 (분포 위치 결정)
  - $\sigma^2$: 분산 (분포 확산 정도 결정)
- **표준정규분포**: $N(0, 1)$ - 평균 0, 표준편차 1
- **특성**:
  - 종형 곡선 (bell-shaped), 대칭
  - 평균 = 중앙값 = 최빈값
  - 68-95-99.7 규칙: 68% data within ±1σ, 95% within ±2σ, 99.7% within ±3σ

---

# 주요 수식 정리

$$\text{Mean: } \bar{x} = \frac{\sum x_i}{n}$$

$$\text{표본분산 (sample variance): } s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$$

$$\text{SE: } SE = \frac{s}{\sqrt{n}}$$

$$\text{95\% CI: } \bar{x} \pm 1.96 \times SE$$

$$\text{Z-score: } Z = \frac{\bar{x} - \mu}{SE}$$

$$\text{Binomial: } P(k) = \binom{n}{k} p^k (1-p)^{n-k}$$

---

# 통계분석 강의노트 Part 2
## t-검정 & ANOVA

---

# 1. t-분포 (t-distribution)

## 정규분포 vs t-분포

| | 정규분포 (z) | t-분포 |
|---|-------------|--------|
| 분산 | 알려져 있음 (σ) | 모름 (s 로 추정) |
| 표본크기 | σ모를 때 n ≥ 30 이면 z 근사 가능 | σ모를 때 항상 t |
| 꼬리 | 얇음 | 두꺼움 (불확실성 반영) |
| 파라미터 | 없음 | 자유도 (df) |

**핵심**: 표본크기보다 **σ를 아는지 여부**가 중요. σ를 모르면 s 를 쓰고 t-분포. n 이 크면 t → z.
- t-분포: 자유도가 증가할수록 정규분포에 가까워짐
- df = n - 1 (one sample)

## t-통계량

$$t = \frac{\bar{x} - \mu}{s/\sqrt{n}}$$

- df = n - 1
- t* (critical value): t-분포표에서 df 와 유의수준으로 결정

---

# 2. One-Sample t-Test

## 가설

- $H_0: \mu = \mu_0$
- $H_A: \mu \neq \mu_0$ (또는 >, <)

## 검정통계량

$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}, \quad df = n - 1$$

## 95% 신뢰구간

$$\bar{x} \pm t^*_{df} \times \frac{s}{\sqrt{n}}$$

**예제: One-sample t-test**

어떤 약의 효과 측정. 표본 n = 25, 평균 8.5, 표준편차 2.1
- $H_0: \mu = 7$ (약 효과 없음)
- $H_A: \mu \neq 7$

$$t = \frac{8.5 - 7}{2.1/\sqrt{25}} = \frac{1.5}{0.42} = 3.57, \quad df = 24$$

t-분포표: df = 24, α = 0.05 (two-tailed) → t* = 2.064
3.57 > 2.064 → p < 0.05 → $H_0$ 기각 (약 효과가 있음)

---

# 3. Two-Sample t-Test (독립표본)

## 가설

- $H_0: \mu_A = \mu_B$ (또는 $\mu_{diff} = 0$)
- $H_A: \mu_A \neq \mu_B$

## Pooled Variance (분산동질가정)

$$s_{pool}^2 = \frac{SS_A + SS_B}{(n_A - 1) + (n_B - 1)}$$

## 검정통계량

$$t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{\frac{s_{pool}^2}{n_A} + \frac{s_{pool}^2}{n_B}}}, \quad df = n_A + n_B - 2$$

## Welch t-test (분산동질가정 없음)

- R 의 기본 방식 (`var.equal = FALSE`)
- df 가 소수점이 될 수 있음

**예제: Two-sample t-test 계산**

남녀 학생의 시험 점수 비교:
- 남학생 (n=10): {78, 82, 75, 88, 90, 85, 79, 83, 81, 87} → mean=82.8, sd=4.76
- 여학생 (n=10): {85, 90, 88, 92, 95, 87, 89, 91, 86, 93} → mean=89.6, sd=3.20

1. Pooled variance:
   $$s_{pool}^2 = \frac{(10-1) \times 4.76^2 + (10-1) \times 3.20^2}{10+10-2} = \frac{204.10 + 92.16}{18} = 16.44$$

2. Pooled sd: $s_{pool} = \sqrt{16.44} = 4.06$

3. t-통계량:
   $$t = \frac{82.8 - 89.6}{\sqrt{\frac{16.44}{10} + \frac{16.44}{10}}} = \frac{-6.8}{\sqrt{3.29}} = \frac{-6.8}{1.81} = -3.75$$

4. df = 10 + 10 - 2 = 18

t-분포표: df = 18, α = 0.05 (two-tailed) → t* = 2.101
|-3.75| = 3.75 > 2.101 → p < 0.05 → $H_0$ 기각 (남녀 점수 차이 있음)

---

# 4. Paired t-Test (비독립표본)

## 적용 경우

- 같은 대상자 두 번 측정 (예: Before/After)
- 짝지음 (matching) 된 표본

## 방법

1. 각 쌍의 차이 $d_i$ 계산
2. 차이값에 one-sample t-test 적용

$$t = \frac{\bar{d} - 0}{s_d/\sqrt{n}}, \quad df = n - 1$$

## 예: 신발무게

| Subject | Shoe On | Shoe Off | 차이 (d) |
|---------|---------|----------|----------|
| 1 | 64.8 | 63.5 | 1.3 |
| 2 | 70.5 | 68.8 | 1.7 |
| 3 | 69.3 | 67.6 | 1.7 |
| 4 | 55.5 | 54.1 | 1.4 |
| 5 | 61.4 | 59.9 | 1.5 |
| 6 | 69.7 | 68.6 | 1.1 |
| 7 | 68.8 | 66.7 | 2.1 |
| 8 | 64.6 | 63.0 | 1.6 |
| 9 | 63.8 | 61.8 | 2.0 |
| 10 | 61.9 | 59.4 | 2.5 |
| 11 | 69.4 | 68.4 | 1.0 |
| 12 | 63.0 | 61.1 | 1.9 |
| 13 | 75.5 | 73.9 | 1.6 |
| 14 | 69.4 | 68.2 | 1.2 |
| 15 | 59.1 | 58.1 | 1.0 |
| **Mean** | 65.78 | 64.21 | **1.57** |
| **SD** | 5.20 | 5.24 | **0.43** |

**계산 단계:**

1. 차이 평균: $\bar{d} = 1.57$
2. 차이 표준편차: $s_d = 0.43$
3. 표준오차: $SE_d = \frac{s_d}{\sqrt{n}} = \frac{0.43}{\sqrt{15}} = 0.111$
4. t-통계량: $t = \frac{\bar{d}}{SE_d} = \frac{1.57}{0.111} = 14.17$
5. df = 15 - 1 = 14

t-분포표: df = 14, α = 0.05 (two-tailed) → t* = 2.145
14.17 > 2.145 → p < 0.001 → $H_0$ 기각 (신발을 신은 상태의 체중이 증가함)

**비교: Two-sample vs Paired**
- Two-sample: p = 0.416 (불 유의) ← 각 표본을 독립으로 간주
- Paired: p = 1.08e-09 (매우 유의) ← **같은 사람이라 짝지음 중요**

---

### 연구 사례: Friday the 13th 교통량 연구 (BMJ 1993)

**연구 설계**: UK 10 개 도로에서 1990-1992 년 Friday 6 일 vs 13 일 교통량 비교
- paired t-test 적용 (같은 도로, 다른 날짜 → 짝지음)
- 결과: 13 일 교통량 유의하게 적음 (t = -2.43, p = 0.03)

**인사이트**: 같은 대상 (도로) 을 두 시점 측정 → paired test 필수. paired 구조를 무시하면 표준오차 추정이 비효율적이고 검정력이 떨어짐.

---

# 5. ANOVA (분산분석)

## 1-Way ANOVA

### 목적

- 3 개 이상 집단의 평균 비교
- 2 집단 비교는 t-test 로 가능하지만, 3 집단 이상에 t-test 를 반복하면 다중비교 문제 발생

### 가설

- $H_0: \mu_1 = \mu_2 = \cdots = \mu_k$ (모든 집단 평균 동일)
- $H_A$: 적어도 한 집단이 다름

### F-통계량

$$F = \frac{MS_{Between}}{MS_{Within}} = \frac{SS_{Between}/df_{Between}}{SS_{Within}/df_{Within}}$$

- $df_{Between} = k - 1$
- $df_{Within} = N - k$

**예제: ANOVA 계산**

3 개 학급 (A, B, C) 의 시험 점수 비교:
- A: n=10, mean=75, variance=25
- B: n=10, mean=80, variance=30
- C: n=10, mean=78, variance=28

전체평균: $\bar{x}_{overall} = (75+80+78)/3 = 77.67$

$$SS_{Between} = 10(75-77.67)^2 + 10(80-77.67)^2 + 10(78-77.67)^2 = 126.67$$
$$SS_{Within} = (10-1)(25+30+28) = 9 \times 83 = 747$$

$$F = \frac{126.67/2}{747/27} = \frac{63.34}{27.67} = 2.29$$

F-분포표: df=(2,27), α=0.05 → F*=3.35
2.29 < 3.35 → p > 0.05 → $H_0$ 기각 안 함 (학급 간 차이가 없음)

### SS 분해

$$SS_{Total} = SS_{Between} + SS_{Within}$$

| | SS | df | MS |
|---|---|---|---|
| Between | $SS_B$ | $k-1$ | $MS_B = SS_B/(k-1)$ |
| Within | $SS_W$ | $N-k$ | $MS_W = SS_W/(N-k)$ |
| Total | $SS_T$ | $N-1$ | |

### F-검정

- F-통계량: $F = \frac{MS_{Between}}{MS_{Within}}$
- **F 분포 (F Distribution)**:
  - 두 카이제곱 분포의 비
  - 자유도 (df1, df2) 로 결정
  - always ≥ 0, right-skewed
- F > F-critical (또는 p < 0.05) → $H_0$ 기각
- ANOVA 로 유의시 → **Post-hoc test** (Bonferroni, Tukey)

### Post-hoc Tests

**왜 필요한가?**
- ANOVA 는 "어느 하나 다르다"만 알려줌, 어디가 다른지는 모름
- 모든 쌍에 t-test 를 하면 Type 1 error 가 증가 (multiple comparisons problem)

**Bonferroni Correction**
- $\alpha_{new} = \alpha / k$ (k = comparison 수)
- 예: 3 개 집단 비교 시 3 회 test → $\alpha = 0.05/3 = 0.017$
- 장점: Type 1 error 통제
- 단점: 너무 보수적, Type 2 error 증가

**Tukey HSD (Honest Significant Difference)**
- All pairwise comparisons of means
- Studentized range distribution 사용
- Bonferroni 보다 power 가 높음
- R: `TukeyHSD(anova_object)`

## Repeated Measures ANOVA (RM-ANOVA)

- 같은 대상자를 여러 번 측정
- Within-subject 변인 분석

### 예: 게임 연구

| | Control | Pedaling | Power-up |
|---|---------|----------|----------|
| Half-Life 2 Importance | 4.21 | 5.04* | 5.29† |
| Skyrim Importance | 3.66 | 4.64* | 5.07† |

- F(2,16) = 7.61, p = 0.005 (HL2)
- F(2,16) = 16.8, p < 0.001 (Skyrim)
- * 또는 † 공유하지 않는 값은 유의하게 다름

**연구 사례: What.Hack 피싱 교육 게임 (CHI 2019)**
- 3 조건: What.Hack vs Anti-Phishing Phil vs PhishLine
- RM-ANOVA: F(2,36) = 18.53, p < .01, η² = .507 (큰 효과)
- What.Hack 점수 증가: M = 0.239, SD = 0.106
- **인사이트**: 역할 수행 게임이 전통 교육보다 효과적 (효과크기 .507)

## Two-Way ANOVA

- 2 개의 독립변수 (factor)
- Main effect × Interaction effect

### 효과

1. **Main Effect A**: A 의 효과 (B 평균)
2. **Main Effect B**: B 의 효과 (A 평균)
3. **Interaction A×B**: A 와 B 의 상호작용

**예제: Two-way ANOVA (2 가지 약물 효과)**

drugA (A0/A1) 와 drugB (B0/B1) 의 효과 분석:

| Source | Df | Sum Sq | Mean Sq | F value | p-value |
|--------|-----|--------|---------|---------|---------|
| drugA | 1 | 153.27 | 153.27 | 17.67 | 0.00017 *** |
| drugB | 1 | 120.06 | 120.06 | 13.84 | 0.00068 *** |
| drugA:drugB | 1 | 0.06 | 0.06 | 0.006 | 0.936 |
| Residuals | 36 | 312.31 | 8.68 | | |

**해석:**
- drugA 주효과: F(1,36) = 17.67, p < 0.001 → **유의** (A1 이 A0 보다 3.9 점 높음)
- drugB 주효과: F(1,36) = 13.84, p < 0.001 → **유의** (B1 이 B0 보다 3.5 점 높음)
- 상호작용: F(1,36) = 0.006, p = 0.936 → **불 유의** (두 약물의 상호작용 없음)

→ 각 약물은 개별적으로 효과가 있으나, 상호작용은 없음

---

## Two-Way RM ANOVA (Repeated Measures)

- 2 개 within-subject factor (같은 대상자 모든 조건 측정)
- 예: 5 channel × 5 activity level × 25 participants

### 효과
- Main Effect Channel
- Main Effect Activity
- Interaction Channel × Activity

---

## Mixed ANOVA (혼합 ANOVA)

- Between-subject factor + Within-subject factor 조합
- 예: Drug (A/B/C, between) × Time (pre/post, within)

### SS 분해
| Source | df |
|--------|-----|
| Between-Subject | |
| - Factor A | a-1 |
| - Error (between) | N-a |
| Within-Subject | |
| - Factor B | b-1 |
| - A × B | (a-1)(b-1) |
| - Error (within) | (N-a)(b-1) |

---

# 6. 비모수검정 (Non-parametric Tests)

## 적용 경우

- 정규분포 가정 불가능
- 서열데이터 (ordinal data)
- 작은 표본

## 검정법

| 모수검정 | 비모수검정 |
|----------|-----------|
| One-sample t | Sign test, Wilcoxon signed-rank |
| Independent t-test | Mann-Whitney U, Wilcoxon rank-sum |
| Paired t-test | Wilcoxon signed-rank |
| 1-Way ANOVA | Kruskal-Wallis |
| Pearson correlation | Spearman's ρ, Kendall's τ |

---

### 연구 사례: Multi-finger Chords 기억 (CHI 2014)

**연구**: Categorical vs Random chord mapping 장기 기억력 비교
- Mann-Whitney U = 6.5, p < 0.001, r = -0.76
- 1 주 후 categorical mapping 우위

**인사이트**: 비모수검정은 서열 데이터에 적합, 효과크기 (r=-0.76) 해석 중요

---

**예제: Mann-Whitney U 계산**

비흡연자 (n=10): 18, 22, 21, 17, 20, 17, 23, 20, 22, 21
흡연자 (n=10): 16, 20, 14, 21, 20, 18, 13, 15, 17, 21

1. 합쳐서 순위 부여 (동점은 평균 순위):
   | 값 | 13 | 14 | 15 | 16 | 17×3 | 18×2 | 20×4 | 21×4 | 22×2 | 23 |
   |---|----|----|----|----|------|------|------|------|------|----|
   | 순위 | 1 | 2 | 3 | 4 | 5,6,7→6 | 8,9→8.5 | 10~13→11.5 | 14~17→15.5 | 18,19→18.5 | 20 |

2. 순위 합:
   - 비흡연자 W₁ = 8.5+18.5+15.5+6+11.5+6+20+11.5+18.5+15.5 = 131.5
   - 흡연자 W₂ = 4+11.5+2+15.5+11.5+8.5+1+3+6+15.5 = 78.5
   - 검증: W₁+W₂ = 210 = 20×21/2 ✓

3. U 통계량:
   $$U_1 = n_1n_2 + \frac{n_1(n_1+1)}{2} - W_1 = 100 + 55 - 131.5 = 23.5$$
   $$U = \min(U_1, U_2) = 23.5$$

R: `wilcox.test(non_smokers, smokers)` → W = 78.5, p ≈ 0.06

---

**예제: Kruskal-Wallis 계산**

3 집단 데이터 (통제, 약물 A, 약물 B):

| 통제 | 약물 A | 약물 B |
|------|--------|--------|
| 10 | 18 | 14 |
| 12 | 20 | 16 |
| 15 | 17 | 13 |
| 11 | 19 | 15 |
| 13 | 21 | 12 |

1. 합쳐서 순위 (동점 평균, 15 개):
   | 값 | 10 | 11 | 12×2 | 13×2 | 14 | 15×2 | 16 | 17 | 18 | 19 | 20 | 21 |
   |---|----|----|------|------|----|------|----|----|----|----|----|----|
   | 순위 | 1 | 2 | 3,4→3.5 | 5,6→5.5 | 7 | 8,9→8.5 | 10 | 11 | 12 | 13 | 14 | 15 |

2. 순위 합:
   - 통제 R₁ = 1+3.5+8.5+2+5.5 = 20.5
   - 약물 A R₂ = 12+14+11+13+15 = 65
   - 약물 B R₃ = 7+10+5.5+8.5+3.5 = 34.5
   - 검증: R₁+R₂+R₃ = 120 = 15×16/2 ✓

3. H 통계량:
   $$H = \frac{12}{15 \times 16} \times \left(\frac{20.5^2}{5} + \frac{65^2}{5} + \frac{34.5^2}{5}\right) - 3 \times 16 = 10.36$$

df = 2, χ²(2) = 9.21 (α=0.01)
10.36 > 9.21 → p < 0.01 → H₀ 기각 (세 집단 중 하나 이상 다름)

R: `kruskal.test(value ~ group, data)` → p < 0.01

---

**예제: Wilcoxon Signed-Rank 계산**

Before: 25, 30, 28, 32, 27
After: 22, 28, 25, 30, 24

1. 차이 d = Before - After: {3, 2, 3, 2, 3}
2. 절대값에 순위: |3|=3 (순위 3,4,5 평균=4), |2|=2 (순위 1,2 평균=1.5)
3. 부호별 순위 합:
   - W⁺ = 4 + 1.5 + 4 + 1.5 + 4 = 15 (모두 양수)
   - W⁻ = 0
4. 검정통계량: V = 15 (R 은 **양의 순위합**을 출력)

R: `wilcox.test(before, after, paired=TRUE)` → V = 15, p = 0.0625

**참고**: 일부 교재에서는 min(W⁺, W⁻) = 0 을 검정통계량으로 사용하지만, R 은 W⁺를 출력.

---

# 7. Chi-Square Test ($\chi^2$)

## 적용

- 범주형 변수 간 독립성 검정
- Contingency table 분석

## 가설

- $H_0$: 두 변수는 독립
- $H_A$: 두 변수는 독립이 아님 (연관됨)

## 기대빈도

$$E_{ij} = \frac{\text{row}_i \times \text{col}_j}{N}$$

## $\chi^2$ 통계량

$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

- df = (행 - 1) × (열 - 1)
- $\chi^2 > \chi^2_{critical}$ → $H_0$ 기각

## 예: 성별과 승진

| | Promoted | Not Promoted | Total |
|---|----------|--------------|-------|
| Male | 21 | 3 | 24 |
| Female | 14 | 10 | 24 |
| **Total** | 35 | 13 | 48 |

**기대빈도 계산:**
- $E_{male,promoted} = 24 \times 35 / 48 = 17.5$
- $E_{male,not} = 24 \times 13 / 48 = 6.5$
- $E_{female,promoted} = 24 \times 35 / 48 = 17.5$
- $E_{female,not} = 24 \times 13 / 48 = 6.5$

**$\chi^2$ 계산:**
$$\chi^2 = \frac{(21-17.5)^2}{17.5} + \frac{(3-6.5)^2}{6.5} + \frac{(14-17.5)^2}{17.5} + \frac{(10-6.5)^2}{6.5}$$
$$= 0.70 + 1.88 + 0.70 + 1.88 = 5.16$$

df = (2-1) × (2-1) = 1
$\chi^2_{critical}$ (α=0.05, df=1) = 3.84

5.16 > 3.84 → p < 0.05 → $H_0$ 기각 (성별과 승진은 연관됨)

---

# 주요 수식 정리

$$\text{One-sample t: } t = \frac{\bar{x} - \mu}{s/\sqrt{n}}, \quad df = n - 1$$

$$\text{Pooled variance: } s_{pool}^2 = \frac{SS_A + SS_B}{n_A + n_B - 2}$$

$$\text{Paired t: } t = \frac{\bar{d}}{s_d/\sqrt{n}}, \quad df = n - 1$$

$$\text{F-statistic: } F = \frac{MS_{Between}}{MS_{Within}}$$

$$\chi^2 = \sum \frac{(O - E)^2}{E}, \quad df = (r-1)(c-1)$$

---

# 통계분석 강의노트 Part 3
## 회귀분석 (Regression)

---

# 1. Simple Linear Regression

## 모델

**모형 (model)**:
$$Y = \beta_0 + \beta_1 X + \varepsilon$$
- $\beta_0, \beta_1$: 모수 (unknown parameters)
- $\varepsilon$: 오차항

**추정 회귀식 (fitted line)**:
$$\hat{y} = b_0 + b_1 x$$
- $b_0, b_1$: 추정치 (estimated coefficients)
- $\hat{y}$: 예측값

## 최소제곱법 (Least Squares)

잔차제곱합 (SSE) 을 최소화하는 직선:

$$\text{minimize } \sum_{i=1}^n (y_i - \hat{y}_i)^2$$

## 기울기와 절편

$$b_1 = \frac{S_{xy}}{S_{xx}} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$

$$b_0 = \bar{y} - b_1 \bar{x}$$

## 잔차 (Residual)

$$e_i = y_i - \hat{y}_i$$

- 관측값 - 예측값
- $SS_{Total} = SS_{Regression} + SS_{Error}$

## R² (결정계수)

$$R^2 = \frac{SS_{Regression}}{SS_{Total}} = 1 - \frac{SS_{Error}}{SS_{Total}}$$

- **해석**: y 의 변동 중 x 로 설명되는 비율
- $r^2 = 0.75$ → 75% 의 변동이 모형으로 설명됨

**예제: 회귀분석 계산**

신장 (cm) 과 체중 (kg) 데이터 (n=5):

| Person | Height (x) | Weight (y) |
|--------|------------|------------|
| 1 | 160 | 60 |
| 2 | 170 | 70 |
| 3 | 175 | 75 |
| 4 | 180 | 80 |
| 5 | 165 | 65 |

$$\bar{x} = 170, \quad \bar{y} = 70$$

$$S_{xx} = (-10)^2 + 0^2 + 5^2 + 10^2 + (-5)^2 = 250$$
$$S_{xy} = (-10)(-10) + 0 \times 0 + 5 \times 5 + 10 \times 10 + (-5)(-5) = 250$$

$$b_1 = \frac{S_{xy}}{S_{xx}} = \frac{250}{250} = 1$$
$$b_0 = \bar{y} - b_1\bar{x} = 70 - 1 \times 170 = -100$$

**예측**: 키 185cm 인 사람 → 체중 = -100 + 1 × 185 = 85 kg

---

# 2. 회귀분석의 조건

1. **선형성 (Linearity)**: x 와 y 의 관계가 선형
2. **정규성 (Normality)**: 잔차가 정규분포
3. **등분산성 (Homoscedasticity)**: 잔차의 분산이 일정
4. **독립성 (Independence)**: 관측치 간 독립

### 잔차plot 으로 조건 확인

- 잔차 vs 예측값: 패턴 없어야 (선형성, 등분산성)
- 잔차 QQ plot: 직선 가까워야 (정규성)

---

# 3. 이상치 (Outliers)

## 유형

1. **High leverage point**: x 방향에서 중심에서 멀리 떨어진 점
2. **Influential point**: 회귀선 기울기에 큰 영향을 주는 점

- influential point 는 보통 leverage 가 크거나 잔차가 커서 회귀계수에 큰 영향을 줌
- 큰 leverage 가 influence 의 중요한 요소이지만, leverage 만으로 결정되지는 않음

## 영향 확인

- 해당 점을 포함/제외하고 회귀선 비교
- 기울기가 크게 변하면 influential

---

# 4. 회귀분석의 추론

## 가설검정

- $H_0: \beta_1 = 0$ (x 와 y 관계없음)
- $H_A: \beta_1 \neq 0$ (x 와 y 관계있음)

## t-통계량

$$t = \frac{b_1 - 0}{SE_{b_1}}, \quad df = n - 2$$

$$SE_{b_1} = \sqrt{\frac{MS_{Error}}{S_{xx}}}$$

## R²와 t-검정

$$t = r \sqrt{\frac{n-2}{1-r^2}}$$

---

# 5. Multiple Regression

## 모델

$$\hat{y} = b_0 + b_1 x_1 + b_2 x_2 + \cdots + b_k x_k$$

## 해석

- $b_1$: 다른 변수를 고정할 때 x₁이 1 단위 증가하면 y 의 평균 변화
- **Adjusted R²**: 변수 수로 보정

$$R^2_{adj} = 1 - (1 - R^2)\frac{n-1}{n-k-1}$$

## F-검정

- $H_0: \beta_1 = \beta_2 = \cdots = \beta_k = 0$ (모든 변수 무의미)
- $H_A$: 적어도 하나의 β ≠ 0

$$F = \frac{MS_{Regression}}{MS_{Error}}, \quad df = (k, n-k-1)$$

## 다중공선성 (Multicollinearity)

**문제**: 예측변수 간 높은 상관관계 → 계수 추정 불안정

### 확인 방법

- **VIF (Variance Inflation Factor)**: $VIF = \frac{1}{1 - R_j^2}$
  - VIF > 5: 주의, > 10: 심각한 다중공선성
- **상관행렬**: 변수 간 r > 0.8

### 해결

- 상관 높은 변수 제거
- Principal Component Analysis (PCA)
- Ridge Regression (규제 회귀)

---

# 6. Logistic Regression

## 적용

- 종속변수가 이분형 (binary) 일 때
- P(Y=1) 예측

## Model

$$\log\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k$$

- 좌변: logit (로그오즈)
- $p = P(Y=1)$

## 확률 예측

$$p = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k)}}$$

## 해석

- $e^{\beta_1}$: x 가 1 단위 증가할 때의 **odds ratio**
- OR = 2 → x 가 1 증가하면 **odds 가 2 배** (확률이 2 배가 아님)

**예제: Logistic Regression**

질병 예측 모델: $\log(\frac{p}{1-p}) = -2 + 0.05 \times \text{age}$

60 세인 사람의 질병 확률:
$$\text{logit} = -2 + 0.05 \times 60 = 1$$
$$p = \frac{1}{1 + e^{-1}} = 0.731$$

→ 60 세면 질병일 확률 73.1%

Odds Ratio 해석:
$$OR = e^{0.05} = 1.051$$
→ 나이 1 세 증가하면 질병 odds 가 1.051 배 (5.1% 증가)

---

### 연구 사례: Donner Party 생존 예측

**데이터**: 1846 년 Donner Party 45 명 (31 명 사망, 14 명 생존)
- 변수: Age, Sex
- 모델: Status ~ Age + Sex (Y=1: 사망, Y=0: 생존)

**결과**:
| Variable | β | OR |
|----------|---|-----|
| Age | 0.077 | 1.08 |
| Sex(M) | -1.2 | 0.30 |

**예측**:
- 25 세 남성: logit = -2.5 + 0.077×25 - 1.2 = -1.77 → p ≈ 14%
- 50 세 남성: logit = -2.5 + 0.077×50 - 1.2 = 0.15 → p ≈ 54%
- **인사이트**: 나이가 10 세 늘어날수록 사망 odds 2.16 배 증가 (e^(0.077×10))
  (Y=1 이 사망으로 코딩되었으므로, 양수 계수 = 사망 odds 증가)

### 연구 사례: 새 사육과 폐암 (매칭 연구)

**연구**: 150 명 (75 폐암 환자, 75 대조군), 나이/성/흡연 매칭
- OR = 3.91 (95% CI: 1.6-9.5)
- **해석**: 새 사육자의 폐암 odds 가 3.9 배 ↑ (case-control 연구이므로 risk 가 아님)
- **인사이트**: 매칭 연구는 교란변수 (나이, 흡연) 통제 효과적

---

# 7. ROC Curve & AUC

## ROC (Receiver Operating Characteristic)

| | 정답 양성 | 정답 음성 |
|---|----------|----------|
| 예측 양성 | TP (True Positive) | FP (False Positive) |
| 예측 음성 | FN (False Negative) | TN (True Negative) |

## 지표

- **Sensitivity (Recall)**: $TP / (TP + FN)$
- **Specificity**: $TN / (TN + FP)$
- **Precision**: $TP / (TP + FP)$
- **Accuracy**: $(TP + TN) / N$

## ROC Curve

- X 축: 1 - Specificity (FPR)
- Y 축: Sensitivity (TPR)
- 다양한 cutoff 에 대한 점들의 연결

## AUC (Area Under Curve)

- 0.5: 무작위 예측
- 0.7-0.8: 적당히 좋음
- 0.8-0.9: 좋음
- > 0.9: 매우 좋음
- **해석**: (0,0) 에서 (1,1) 까지 ROC 곡선 아래 면적
- **의미**: 임의의 양성 샘플이 임의의 음성 샘플보다 높은 확률로 분류될 확률

**참고**: AUC 는 여러 threshold 에 대한 ROC 곡선 전체의 요약. 아래 예제는 한 cutoff 에서의 분류 성능지표 계산:

**예제: Confusion Matrix 계산 (단일 cutoff)**

100 개 샘플 (75 양성, 25 음성)

| | 실제 양성 | 실제 음성 |
|---|----------|----------|
| 예측 양성 | 50 (TP) | 5 (FP) |
| 예측 음성 | 25 (FN) | 20 (TN) |

지표 계산:
- Accuracy = (50+20)/100 = **0.70**
- Precision = 50/(50+5) = **0.91**
- Recall (Sensitivity) = 50/(50+25) = **0.67**
- Specificity = 20/(20+5) = **0.80**
- F1 = 2 × (0.91×0.67)/(0.91+0.67) = **0.77**

---

# 8. Overfitting & Cross-Validation

## Overfitting

- 학습데이터에서는 성능 우수
- 새로운 데이터에서는 성능 저하
- 모델이 너무 복잡할 때 발생

## Cross-Validation

- 데이터를 k-fold 로 분할
- k-1 fold 학습, 1 fold 테스트 (k 번 반복)
- 평균 성능으로 모델 평가

### 5-fold Cross-Validation

| Split | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
|-------|-------|-------|-------|-------|-------|
| 1 | **test** | train | train | train | train |
| 2 | train | **test** | train | train | train |
| ... | ... | ... | ... | ... | ... |

---

# 9. R 구현

## Simple Regression

```r
model <- lm(y ~ x, data = df)
summary(model)

# 결과 해석
# Coefficients: Estimate, Std. Error, t value, Pr(>|t|)
# R-squared, F-statistic
```

## Multiple Regression

```r
model <- lm(y ~ x1 + x2 + x3, data = df)
```

## Logistic Regression

```r
model <- glm(Y ~ x1 + x2, data = df, family = binomial)
summary(model)

# 확률 예측
predict(model, newdata, type = "response")
```

## AUC

```r
library(pROC)
roc_obj <- roc(df$Y, predict(model, type = "response"))
auc(roc_obj)
```

---

# 주요 수식 정리

$$\text{Regression line: } \hat{y} = b_0 + b_1 x$$

$$\text{Slope: } b_1 = \frac{S_{xy}}{S_{xx}}$$

$$R^2 = \frac{SS_{Regression}}{SS_{Total}} = 1 - \frac{SS_{Error}}{SS_{Total}}$$

$$\text{Logistic: } \log\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 x$$

$$\text{AUC: 0.5(무작위) ~ 0.7(참고) ~ 0.8(양호) ~ 0.9(우수) ~ 1.0(완벽)}$$
(경험적 해석 기준, 문맥/불균형에 따라 달라질 수 있음)

---

# 통계분석 강의노트 Part 4
## 머신러닝 (Machine Learning)

---

# 1. 머신러닝 기초

## 학습 유형

### 지도학습 (Supervised Learning)
- **Classification**: 범주형 결과 (예: 스팸/일반)
- **Regression**: 수치형 결과 (예: 가격 예측)

### 비지도학습 (Unsupervised Learning)
- **Clustering**: 그룹화 (예: k-means)
- **Dimensionality Reduction**: 차원 축소 (예: PCA)

## Train/Test Split

- **Train set (80-90%)**: 모델 학습
- **Test set (10-20%)**: 모델 평가
- **Overfitting 방지**: 학습 데이터로 평가 X

---

# 2. Naive Bayes

## 베이즈정리

$$P(A \mid B) = \frac{P(B \mid A) \times P(A)}{P(B)}$$

문서 분류에 적용:
$$P(\text{Category} \mid \text{Document}) \propto P(\text{Document} \mid \text{Category}) \times P(\text{Category})$$

## Naive 가정

- 모든 단어가 **독립적**이라고 가정
- 실제로는 독립이 아니지만 계산이 간편

## 예: "quick rabbit" 분류

**학습 데이터:**

| Sentence | Label |
|----------|-------|
| 'the quick rabbit jumps fences' | good |
| 'make quick money at casino' | bad |
| 'the quick brown fox jumps' | good |
| 'quick silver is fast' | good |
| 'rabbit is clever' | bad |

**단어 빈도 (단순화):**

| 단어 | good | bad |
|------|------|-----|
| quick | 3 | 1 |
| rabbit | 1 | 1 |
| 총 단어 | 15 | 10 |

**사전확률:**
- $P(\text{good}) = 3/5 = 0.6$
- $P(\text{bad}) = 2/5 = 0.4$

**조건부 확률 (스무딩 없이 단순 빈도):**
- $P(\text{quick} \mid \text{good}) = 3/15 = 0.2$
- $P(\text{rabbit} \mid \text{good}) = 1/15 = 0.067$
- $P(\text{quick} \mid \text{bad}) = 1/10 = 0.1$
- $P(\text{rabbit} \mid \text{bad}) = 1/10 = 0.1$

**"quick rabbit" 분류:**

$$\begin{aligned}
P(\text{good} \mid \text{quick rabbit}) &\propto 0.2 \times 0.067 \times 0.6 = 0.008 \\
P(\text{bad} \mid \text{quick rabbit}) &\propto 0.1 \times 0.1 \times 0.4 = 0.004
\end{aligned}$$

0.008 > 0.004 → **"quick rabbit" → good 로 분류**

**로그 확률로 계산 (더 안정적):**

$$\begin{aligned}
\log P(\text{good} \mid \text{quick rabbit}) &= \log(0.2) + \log(0.067) + \log(0.6) \\
&= -1.61 - 2.71 - 0.51 = -4.83 \\
\log P(\text{bad} \mid \text{quick rabbit}) &= \log(0.1) + \log(0.1) + \log(0.4) \\
&= -2.30 - 2.30 - 0.92 = -5.52
\end{aligned}$$

-4.83 > -5.52 → **good 로 분류** (로그 확률이 더 큼)

---

# 3. Decision Tree

## 기본원리

- **Greedy algorithm**: 각 노드에서 최선의 분할 선택
- **Entropy 감소**: 가장 많이 줄이는 feature 선택

## Entropy (무질서도)

$$H(X) = -\sum_{i=1}^n p_i \log_2 p_i$$

- H = 0: 완전 예측 가능 (모든 경우 동일)
- H = 1: 완전 랜덤 (50:50)

**예제: Entropy 계산**

데이터: 10 개 샘플 중 6 개는 class A, 4 개는 class B

$$H = -0.6 \log_2(0.6) - 0.4 \log_2(0.4) = 0.6 \times 0.737 + 0.4 \times 1.322 = 0.971$$

Feature "Age"로 분할:
- Age < 30: 3 개 (A=2, B=1) → H = 0.92
- Age ≥ 30: 7 개 (A=4, B=3) → H = 0.99

**Weighted Entropy**: $(3/10) \times 0.92 + (7/10) \times 0.99 = 0.969$

**Information Gain**: $0.971 - 0.969 = 0.002$

→ 이 feature 는 정보 획득이 적음 (나쁜 분할)

### 예

| Dataset | p | H |
|---------|---|---|
| [M, M, M, M] | 0 | 0 |
| [M, M, M, F] | 0.25 | 0.81 |
| [M, M, F, F] | 0.5 | 1 |

## Information Gain

$$\text{Gain} = H(\text{before}) - H(\text{after})$$

- Gain 이 가장 큰 feature 를 선택
- 재귀적으로 분할

### 예: 영화 성공 예측

| Film | Country | BigStar | Genre | Success |
|------|---------|---------|-------|---------|
| 1 | USA | Yes | SciFi | ✓ |
| 2 | USA | No | Comedy | ✗ |
| ... | ... | ... | ... | ... |

1. **Entropy(Success)** = 1 (5:5)
2. **Gain(Country)** = 0.276 ← 최대
3. **Gain(BigStar)** = 0.035
4. **Gain(Genre)** = 0.174

→ Country 로 먼저 분할

## R/Python 구현

```python
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

---

# 4. Random Forest

## Ensemble Method

- **Bagging**: 여러 모델 학습 → 결과 결합
- **다양성 (Diversity)**: 모델들이 서로 다름이 중요

## 알고리즘

1. K 개의 bootstrap sample 생성 (반복추출)
2. 각 sample 로 decision tree 학습
   - 각 node 에서 m 개 feature 랜덤 선택 ($m \approx \sqrt{p}$)
   - Best split 선택
3. 투표 (majority vote) 로 최종 예측

## 장점

- 구현 용이
- 병렬 처리 가능
- 과적합 relatively 적음
- Feature importance 추출 가능

## 단점

- 해석 어려움 (black box)
- DNN 보다 정확도 낮을 수 있음

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
```

---

# 5. Support Vector Machine (SVM)

## 기본원리

- **Margin maximization**: 분류경계와 가장 가까운 데이터의 거리 최대화
- **Support vectors**: margin 정의에 참여하는 점들만 중요

## Hard Margin

$$\min \frac{1}{2}||w||^2, \quad \text{s.t. } y_i(w \cdot x_i + b) \geq 1$$

## Soft Margin (실제 사용)

$$\min \frac{1}{2}||w||^2 + C\sum\xi_i$$

- $\xi_i$: slack variable (오류 허용)
- **C**: penalty parameter (C > 0)
  - C 가 매우 크면: 오류를 강하게 벌점 → hard margin에 가까워짐
  - C 가 작으면: 오류 허용 증가 → margin 을 넓히려는 경향

## Hinge Loss

$$\text{Loss} = \max(0, 1 - y_i(w \cdot x_i + b))$$

```python
from sklearn import svm
model = svm.SVC(kernel='linear', C=1.0)
model.fit(X_train, y_train)
```

---

# 6. k-Nearest Neighbor (k-NN)

## 알고리즘

1. 테스트샘플에 대해 distance 계산
2. k 개의 가장 가까운 학습샘플 선택
3. classification: majority vote
4. regression: 평균

## 파라미터

- **Distance metric**: Euclidean, Manhattan
- **k**: neighbor 수 (작으면 overfit, 크면 underfit)
- **Weighting**: 거리 가중치 (optional)

## 특징

- **Lazy learning**: 학습단계 없음 (전체 데이터 저장)
- **Non-parametric**: 분포 가정 없음
- **k=1**: 1-NN (overfit 경향)

---

# 7. k-Means Clustering

## 알고리즘

1. k 개의 중심 (centroid) 랜덤 초기화
2. 각 점을 가장 가까운 center 에 할당
3. 각 cluster 의 mean 으로 center 업데이트
4. 2-3 단계 수렴할 때까지 반복

## 목적함수

$$\text{minimize } \sum_{i=1}^k \sum_{x \in C_i} ||x - \mu_i||^2$$

- $C_i$: i 번째 cluster
- $\mu_i$: i 번째 centroid

## k 결정

- **Elbow method**: within-cluster sum of squares plot
- **Silhouette score**: 1 에 가까울수록 좋음

**예제: k-Means Clustering (k=2)**

데이터: 5 개의 2 차원 점
- A(1, 2), B(1.5, 1.8), C(5, 8), D(6, 8), E(8, 6)

**1 단계**: 중심 초기화 → C1(1, 2), C2(5, 8)

**2 단계**: 거리 계산 및 할당
- A to C1: $\sqrt{(1-1)^2 + (2-2)^2} = 0$
- A to C2: $\sqrt{(1-5)^2 + (2-8)^2} = 7.21$
- → A 를 C1 에 할당

| Point | dist to C1 | dist to C2 | Cluster |
|-------|------------|------------|---------|
| A(1,2) | 0.00 | 7.21 | 1 |
| B(1.5,1.8) | 0.54 | 7.12 | 1 |
| C(5,8) | 7.21 | 0.00 | 2 |
| D(6,8) | 7.81 | 1.00 | 2 |
| E(8,6) | 8.06 | 3.61 | 2 |

**3 단계**: 중심 업데이트
- C1' = (A+B)/2 = ((1+1.5)/2, (2+1.8)/2) = (1.25, 1.9)
- C2' = (C+D+E)/3 = ((5+6+8)/3, (8+8+6)/3) = (6.33, 7.33)

→ 반복할 때까지

---

# 8. Principal Component Analysis (PCA)

## 목적

- **차원 축소**: 고차원 → 저차원
- **정보 보존**: 분산을 최대한 유지

## 원리

1. covariance matrix 계산
2. eigenvalue, eigenvector 계산
3. **Principal Component** = eigenvector (큰 eigenvalue 순)
4. 데이터 projection

## 특징

- 1st PC: 가장 큰 분포 방향
- 2nd PC: 1st 와 orthogonal, 두 번째로 큰 분포
- PCs: uncorrelated

---

# 9. 성능평가 (Evaluation)

## Confusion Matrix

| | Actual Positive | Actual Negative |
|---|----------------|-----------------|
| **Predicted Positive** | TP | FP |
| **Predicted Negative** | FN | TN |

## 지표

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall (Sensitivity)} = \frac{TP}{TP + FN}$$

$$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

## 선택 가이드

| 상황 | 중요지표 |
|------|---------|
| 암 진단 | Recall (거짓 음성 최소화) |
| 스팸 필터 | Precision (거짓 양성 최소화) |
| 균형 중요 | F1-score |

---

# 10. Python/scikit-learn

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model fit & predict
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
from sklearn import metrics
print(metrics.confusion_matrix(y_test, y_pred))
print(metrics.accuracy_score(y_test, y_pred))
print(metrics.roc_auc_score(y_test, y_proba))

# Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
```

---

# 통계분석 강의노트 Part 5
## 종합 & 심화

---

# 1. 연구디자인 & 통계분석 선택

## 분석방법 선택 가이드

### 종속변수 (Response) 유형

| Response | Predictor | 분석방법 |
|----------|-----------|---------|
| 수치형 | 1 개 범주 (2 수준) | t-test |
| 수치형 | 1 개 범주 (3+ 수준) | ANOVA |
| 수치형 | 1 개 수치 | Simple regression |
| 수치형 | 다변수 | Multiple regression |
| 범주형 | 범주형 | Chi-square |
| 범주형 | 다변수 | Logistic regression |

### 실험 설계

| 설계 | 분석 |
|------|------|
| Between-subjects (독립) | Independent t-test, 1-way ANOVA |
| Within-subjects (반복) | Paired t-test, RM-ANOVA |
| Mixed (혼합) | Mixed ANOVA |

---

# 2. 효과크기 (Effect Size)

## 왜 필요할까?

- p-value 는 표본크기에 영향 받음
- **실질적 의미**를 판단하려면 효과크기 필요

## Cohen's d (t-test)

$$d = \frac{\bar{x}_1 - \bar{x}_2}{s_{pooled}}$$

| d | 해석 |
|---|------|
| 0.2 | 작은 효과 |
| 0.5 | 중간 효과 |
| 0.8 | 큰 효과 |

**예제: Cohen's d 계산**

- 통제집단: n₁=20, mean₁=65, SD₁=10
- 실험집단: n₂=20, mean₂=75, SD₂=12

$$s_{pooled} = \sqrt{\frac{(20-1) \times 10^2 + (20-1) \times 12^2}{20+20-2}} = \sqrt{\frac{1900+2736}{38}} = 11.05$$

$$d = \frac{75 - 65}{11.05} = 0.91$$

→ 큰 효과 (두 집단 평균 차이가 0.9 표준편차)

## Eta-squared (ANOVA)

$$\eta^2 = \frac{SS_{Between}}{SS_{Total}}$$

- ANOVA 의 R²에 해당
- 0.01 (작음), 0.06 (중간), 0.14 (큼)

---

# 3. Power Analysis

## Power ($1-\beta$)

- $H_A$가 참일 때 $H_0$를 기각할 확률
- 일반적으로 0.80 이상 목표

## Power 영향요인

1. **효과크기**: 효과 클수록 ↑
2. **표본크기**: n 클수록 ↑
3. **유의수준**: α 커질수록 ↑

**예제: Power 계산 (독립 2 표본 t-test)**

새로운 교육 방법이 효과 있을 것으로 예상됨:
- 통제군 평균: μ₁ = 70
- 실험군 기대 평균: μ₂ = 75 (효과크기 d = 0.5)
- 표준편차: σ = 10
- 유의수준: α = 0.05

1. 검정력 계산 (각 집단 n = 30):
   - 효과크기: $d = \frac{75-70}{10} = 0.5$ (중간 효과)
   - 각 집단 n = 30, α = 0.05, d = 0.5 일 때 power ≈ 0.53 (비충분)

2. 충분한 power(0.80) 을 위한 표본크기:
   - d = 0.5, α = 0.05, power = 0.80 → **각 집단 n ≈ 64 필요** (총 128 명)
   - (G*Power 등의 software 로 계산)

**Power 표본크기 산정 표 (α = 0.05, power = 0.80)**

| 효과크기 (d) | 필요한 n (각 집단) |
|-------------|-------------------|
| 0.2 (작음) | 393 |
| 0.5 (중간) | 64 |
| 0.8 (큼) | 26 |

## 표본크기 산정

- 연구 전 power analysis 필수
- G*Power 등의 software 사용
- Post-hoc power: 의미 없음 (이미 데이터 있으면 p-value 충분)

---

# 4. Multiple Comparisons

## 문제

- k 번 검정하면 False positive 확률 증가
- Family-wise error rate: $1 - (1-\alpha)^k$

## Bonferroni Correction

$$\alpha_{adjusted} = \frac{\alpha}{k}$$

- k = 10 번 검정 → α = 0.005
- 보수적 (conservative)

## False Discovery Rate (FDR)

- Benjamini-Hochberg method
- Bonferroni 보다 덜 보수적

---

# 5. Assumptions Check

## 정규성 (Normality)

### 확인방법

1. **QQ plot**: 점들이 직선 가까움
2. **Shapiro-Wilk test**: p > 0.05
3. **Histogram**: 종형

### 대처

- 표본이 충분히 크면: 표본평균의 분포는 CLT 로 정규분포에 가까워짐 (하지만 원자료 정규화는 아님)
- 왜도 심함: **log transformation**
  - **장점**: outlier 영향 감소, 모델링 쉬움
  - **단점**: 해석 어려움 (log 값은 직관적이지 않음)
  - 예: salary, housing prices, browsing time
- 여전히 안됨: 비모수검정

## 등분산성 (Homogeneity of Variance)

### 확인방법

- **Levene's test**: p > 0.05
- **Residual plot**: 퍼짐 일정

### 대처

- Welch t-test (분산동질 X 가정)
- Transformation

## 독립성 (Independence)

- 실험 설계 단계에서 확보
- 위반시: mixed model, time series

---

# 6. 통계분석 보고서

## APA 스타일

### t-test

> "A two-sample t-test indicated that the treatment group (M = 5.2, SD = 1.1) scored significantly higher than the control group (M = 4.3, SD = 1.3), t(58) = 2.84, p = .006, d = 0.74."

### ANOVA

> "A one-way ANOVA revealed a significant effect of condition on response time, F(2, 57) = 5.67, p = .006, $\eta^2$ = 0.17. Post-hoc comparisons using Bonferroni correction indicated..."

### Regression

> "Multiple regression analysis showed that age and income significantly predicted satisfaction, $R^2$ = 0.34, F(2, 97) = 25.3, p < .001. Age was a significant predictor ($\beta$ = −0.23, p = .012), as was income ($\beta$ = 0.41, p < .001)."

---

# 7. Common Pitfalls

## p-hacking

- 여러 분석 시도 후 유의한 결과만 보고
- **Pre-registration** 로 방지

## Selection Bias

- 표본이 모집단 대표하지 않음
- Random sampling 필수

## Ecological Fallacy

- 집단수준 상관관계 → 개인수준으로 일반화 X

## Simpson's Paradox

- 전체 데이터와 하위그룹 데이터 방향 반대
- Confounding variable 확인

## Overfitting

- 학습데이터에서만 좋음
- Cross-validation, train/test split 로 방지

---

# 8. R/Python Cheat Sheet

## R

```r
# 데이터
df <- read.csv("data.csv")
summary(df)

# 시각화
hist(df$x)
boxplot(y ~ group, data = df)
plot(x, y)

# 통계
t.test(y ~ group, data = df)
aov(y ~ group, data = df)
lm(y ~ x1 + x2, data = df)
chisq.test(table)

# 비모수
wilcox.test(y ~ group, data = df)  # Mann-Whitney U
wilcox.test(before, after, paired=TRUE)  # Wilcoxon signed-rank
kruskal.test(y ~ group, data = df)  # Kruskal-Wallis
friedman.test(y ~ treatment | subject, data = df)  # Friedman
cor.test(x, y, method = "spearman")

# ROC Curve (pROC package)
library(pROC)
model <- glm(y ~ x1 + x2, data = df, family = binomial)
pred <- predict(model, type = "response")
roc_obj <- roc(df$y, pred)
plot(roc_obj)
auc(roc_obj)  # AUC 값
```

## Python

```python
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터
df = pd.read_csv("data.csv")
df.describe()

# 시각화
sns.histplot(df['x'])
sns.boxplot(x='group', y='y', data=df)
sns.scatterplot(x='x', y='y', data=df)

# 통계
stats.ttest_ind(a, b)
stats.f_oneway(*groups)
stats.chi2_contingency(table)
stats.spearmanr(x, y)

# 회귀
import statsmodels.api as sm
model = sm.OLS(y, sm.add_constant(X)).fit()
print(model.summary())

# 머신러닝
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix
)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model fit
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Evaluation metrics
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall:    {recall_score(y_test, y_pred):.3f}")
print(f"F1:        {f1_score(y_test, y_pred):.3f}")
print(f"AUC:       {roc_auc_score(y_test, y_proba):.3f}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

# Cross-validation (5-fold)
cv_scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')
print(f"CV AUC: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
```

---

# 9. 통계기호 정리

| 기호 | 의미 |
|------|------|
| $\mu$ | 모평균 |
| $\bar{x}$ | 표본평균 |
| $\sigma$ | 모표준편차 |
| $s$ | 표본표준편차 |
| $\sigma^2$ | 모분산 |
| $s^2$ | 표본분산 |
| $N$ | 모집단 크기 |
| $n$ | 표본 크기 |
| $\alpha$ | 유의수준 (Type 1 error) |
| $\beta$ | Type 2 error |
| $1-\beta$ | Power |
| $p$ | 확률 / p-value |
| $H_0$ | 귀무가설 |
| $H_A$ | 대립가설 |
| $r$ | 상관계수 |
| $R^2$ | 결정계수 |
| $\beta_i$ | 회귀계수 |
| $df$ | 자유도 |
| $SE$ | Standard Error |

---

# 10. 추가 자료

## 교재

- OpenIntro Statistics (무료): https://www.openintro.org/book/os/
- VassarStats: http://vassarstats.net/

## 온라인 계산기

- VassarStats: 다양한 통계 검정
- R: `?functionname`
- Python: `help(function)`

## 데이터셋

- OpenIntro: http://www.openintro.org/stat/data/
- UCI ML Repository
- Kaggle

---

# 종합 정리

## 5 개 Part 요약

| Part | 주제 |
|------|------|
| 1 | 기본개념, 변수, 확률, CLT, 신뢰구간 |
| 2 | t-test, ANOVA, 비모수, Chi-square |
| 3 | 회귀분석 (Simple, Multiple, Logistic), R², ROC/AUC |
| 4 | 머신러닝 (Bayes, Decision Tree, Random Forest, SVM, k-NN, k-Means, PCA) |
| 5 | 효과크기, Power, Multiple Comparisons, Reporting, Pitfalls |

## 핵심 메시지

1. **연구디자인이 가장 중요**: 분석으로 고칠 수 없는 편향은 많음
2. **가정 확인 필수**: 모든 검정은 가정을 기반으로 함
3. **p-value 만 믿지 말기**: 효과크기, 신뢰구간 함께 보고
4. **Reproducibility**: 분석과정 문서화, 코드는 공유
5. **Continuous Learning**: 통계/ML은 계속 발전하는 분야