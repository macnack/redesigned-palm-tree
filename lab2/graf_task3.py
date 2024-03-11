

knc = (21826.0, 37183.0)
svc = (6082.0, 8183.0)
rnf = (425873.0, 429796.0)
dtc = (3667.0, 3588.0)
mlp = (5274.0, 5575.0)

# create histogram
import matplotlib.pyplot as plt
import numpy as np

labels = ['KNeighborsClassifier', 'SVC', 'RandomForestClassifier', 'DecisionTreeClassifier', 'MLPClassifier']
# change order from first to last
labels.reverse()

single = [knc[0], svc[0], rnf[0], dtc[0], mlp[0]]
single.reverse()
batch = [knc[1], svc[1], rnf[1], dtc[1], mlp[1]]
batch.reverse()
# y label time
plt.ylabel('Time [ms]')
# x label classifier
plt.xlabel('Classifier')
# title
plt.title('Single and batch prediction time')
# x axis
x = np.arange(len(labels))
plt.xticks(x, labels)
# plot
plt.bar(x - 0.2, single, 0.4, label='Single prediction')
plt.bar(x + 0.2, batch, 0.4, label='Batch prediction')
# legend
plt.legend()
# show plot
plt.show()
plt.savefig('graf_task3.png')