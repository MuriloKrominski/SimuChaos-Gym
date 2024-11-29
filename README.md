# **SimuChaos-Gym**

## **Statistical Simulator for Disorder Impact on the Smart Fit Network**

The **SimuChaos-Gym** is a simulator designed to explore how small behavioral patterns in shared environments can lead to significant system-wide impacts. Using Monte Carlo-based simulations, the project analyzes the balance between organized and disorganized users in the Free Weights section of **Smart Fit** gyms. It quantifies the effects of disorder and helps to understand how individual actions can influence the collective experience.

Grounded in the real infrastructure of **Smart Fit**, the largest gym network in Latin America, **SimuChaos-Gym** presents practical scenarios and tangible results. Beyond identifying problems, the simulator proposes solutions to mitigate disorder and even chaos. Perfect for gym managers, behavior researchers, or the curious, the project provides useful and actionable insights.

More than just a study about gyms, **SimuChaos-Gym** is a tool for improving any shared environment. Its findings highlight how simple interventions can bring organization and harmony, making them applicable to public spaces, logistics, and other systems. Discover how data can transform disorder into efficiency and positively impact collective experiences.

Created by ([Murilo Krominski](https://github.com/murilokrominski)), inspired by a project by [Rodrigo Soares Tadewald](https://github.com/rtadewald).

---

> **Inspirational Quote:**  
> *"The major societal transformations are often caused by noisy minorities."*  
> — Friedrich Hayek

---

## **Why Smart Fit?**

**Smart Fit**, one of the largest gym networks in Latin America, offers a standardized and widely accessible infrastructure, ideal for behavioral and operational analyses. This project is based on characteristics observed across its locations, including:

- **Equipment standards:** Quantity and weight of dumbbells available in the gyms.
- **User profile:** Diversity of users and behaviors, reflecting a microcosm of shared environments.
- **Impact on organization:** The project demonstrates how minor deviations in individual behavior can significantly affect the collective experience.

The analysis not only provides insights to optimize gym operations but also serves as a foundation for awareness and continuous improvement initiatives.

---

## **Objective**

To quantify the impact of disorganized behavior from a minority of users on the arrangement of dumbbells in the Free Weights section of **Smart Fit** gyms. The simulator enables:

- Calculating the probability of disorder reaching critical levels by the end of the day.
- Estimating the minimum number of disorganized users needed to generate "chaos."
- Identifying trends and suggesting practices to reduce negative impacts, fostering a smoother and more enjoyable experience for all gym users.

---

## **Database: Smart Fit Network**

To ensure simulation relevance, **SimuChaos-Gym** uses real data about **Smart Fit's** infrastructure, considering:

### **Number of Dumbbells Available**

- **Average number:** 60 pairs per gym.
- **Weight range:** 10 kg to 36 kg, in 2 kg increments.
- **Typical dumbbell distribution:**

| **Weight (kg)** | **Number of Pairs** | **Observation**                         |
|------------------|---------------------|-----------------------------------------|
| 10               | 2                   | Available in 25% of locations.          |
| 12               | 2                   |                                         |
| 14               | 2                   |                                         |
| 16               | 3                   |                                         |
| 18               | 6                   | Lightest dumbbell in 75% of locations. |
| 20–30            | 5 per weight        |                                         |
| 32–34            | 4 per weight        |                                         |
| 36               | 2                   | Heaviest weight available.             |

These data are standardized based on observations from various **Smart Fit** gyms and can be adjusted for specific unit or scenario analyses.

---

## **Simulated Behaviors**

### **Organized User**
- Always returns dumbbells to their designated location based on weight.
- If the corresponding location is occupied, places the dumbbells on the nearest available rack.

### **Disorganized User**
- Returns dumbbells to random locations, disregarding the weight-to-rack correspondence.

---

## **Simulation Example**

The simulator measures the impact of different proportions of organized and disorganized users. Scenarios range from predominantly organized environments to critical ones with a higher presence of disorganized behavior.

---

## **Result Analysis**

### **Mean Ranges**
Mean values vary by scenario, representing the proportion of organized and disorganized users. Below are three simulated scenarios:

#### **Scenario 1 (90% organized, 10% disorganized):**  
- **Average disorder:** **10.77 disorganized units.**  
- **Confidence interval:** **(10.61 to 10.92).**  
- Predominantly organized users keep disorder low and predictable.

#### **Scenario 2 (75% organized, 25% disorganized):**  
- **Average disorder:** **22.09 disorganized units.**  
- **Confidence interval:** **(21.88 to 22.29).**  
- Significant system impact due to 25% disorganized users.

#### **Scenario 3 (60% organized, 40% disorganized):**  
- **Average disorder:** **31.47 disorganized units.**  
- **Confidence interval:** **(31.26 to 31.68).**  
- Near-equal proportions of organized and disorganized users result in critical disorder.

---

## **Simulated Scenarios**

### **Scenario 1 (90% organized, 10% disorganized)**

**Input:**
- **Number of simulations:** 1,000.
- **Total users:** 60.
- **Disorganized users:** 6.

**Results:**
- **Average disorder:** 10.77.
- **Standard deviation:** 2.44.
- **Confidence interval (95%):** (10.61, 10.92).
- **Histogram generation time:** 18.22 seconds.
- **Impact chart generation time:** 30.08 seconds.

Graphs available in the repository.

---

### **Scenario 2 (75% organized, 25% disorganized)**

**Input:**
- **Number of simulations:** 1,000.
- **Total users:** 60.
- **Disorganized users:** 15.

**Results:**
- **Average disorder:** 22.09.
- **Standard deviation:** 3.33.
- **Confidence interval (95%):** (21.88, 22.29).
- **Histogram generation time:** 20.46 seconds.
- **Impact chart generation time:** 33.35 seconds.

Graphs available in the repository.

---

### **Scenario 3 (60% organized, 40% disorganized)**

**Input:**
- **Number of simulations:** 1,000.
- **Total users:** 60.
- **Disorganized users:** 24.

**Results:**
- **Average disorder:** 31.47.
- **Standard deviation:** 3.42.
- **Confidence interval (95%):** (31.26, 31.68).
- **Histogram generation time:** 30.11 seconds.
- **Impact chart generation time:** 25.46 seconds.

Graphs available in the repository.

---

## **Conclusion**

The scenarios demonstrate the growing impact of disorder as the proportion of disorganized users increases:

- **Scenario 1** represents an organized environment with minimal impact.  
- **Scenario 2** shows a moderately affected environment due to disorder.  
- **Scenario 3** highlights an environment where disorder predominates, requiring mitigation measures.

---

## **Expected Outcomes**

- **Probability of complete disorder:** What are the chances that all dumbbells end up misplaced by the end of the day?
- **Incremental impact:** How does an increase in disorganized users affect overall organization?
- **Impact charts:** Clear visualizations to illustrate the results.

---

## **Why is this important for Smart Fit?**

Disorder directly affects customer experience. This simulator provides insights to:

- **Practical interventions:** Justify educational campaigns or structural improvements.  
- **Customer satisfaction:** Ensure an organized environment for users.  
- **Operational innovation:** Apply technology for continuous optimization.

---

## **Collaboration and Licensing**

**License:**  
MIT License

**Authors:**  
- **Murilo Krominski** ([GitHub](https://github.com/murilokrominski))  
- Inspired by **Rodrigo Soares Tadewald** ([GitHub](https://github.com/rtadewald))  