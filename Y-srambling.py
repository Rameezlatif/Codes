#Y-Scrambling Model Validation (Used to test the model of the performance, Read the article before applying https://www.geeksforgeeks.org/y-scrambling-for-model-validation/)
import numpy as np
shuffled_r2 = []
for i in range(3564):
    np.random.shuffle(Y)
      
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X, Y)
      
    ypred = model.predict(X)
    shuffled_r2.append(r2_score(Y,ypred))
  
print(shuffled_r2[:20])

