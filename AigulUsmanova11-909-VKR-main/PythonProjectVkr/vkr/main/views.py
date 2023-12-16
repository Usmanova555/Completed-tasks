from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
import csv
import io
import os

from .forms import LoginUserForm, FieldForm, ColumnsForm
from .models import CsvFile, ColumnsCount, FieldName


def index(request):
    data = {
        'title': 'Главная страница',
    }
    if request.method == 'POST':
        formColumns = ColumnsForm(request.POST)
        if formColumns.is_valid():
            formColumns.save()
            return redirect('secondPage')

    formColumns = ColumnsForm()
    return render(request, 'main/index.html', {'data': data, 'formColumns': formColumns})


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def model(io_string):
    newEntityNum = FieldName.objects.all().last()
    newEntityNum = str(newEntityNum)
    if newEntityNum != 'None':
        newEntityNum = int(newEntityNum)
    path = ''

    if newEntityNum == 'None':
        columns = ColumnsCount.objects.all()
        columnCount = 0
        for column in columns:
            columnCount = str(column)

        match columnCount:
            case '3':
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    _, created = CsvFile.objects.update_or_create(
                        num=column[0],
                        data=column[1],
                        entity=column[2],
                    )

            case '4':
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    _, created = CsvFile.objects.update_or_create(
                        num=column[0],
                        data=column[1],
                        entity=column[2],
                        entity2=column[3],
                    )

            case '5':
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    _, created = CsvFile.objects.update_or_create(
                        num=column[0],
                        data=column[1],
                        entity=column[2],
                        entity2=column[3],
                        entity3=column[4],
                    )

            case '6':
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    _, created = CsvFile.objects.update_or_create(
                        num=column[0],
                        data=column[1],
                        entity=column[2],
                        entity2=column[3],
                        entity3=column[4],
                        entity4=column[5],
                    )

            case '7':
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    _, created = CsvFile.objects.update_or_create(
                        num=column[0],
                        data=column[1],
                        entity=column[2],
                        entity2=column[3],
                        entity3=column[4],
                        entity4=column[5],
                        entity5=column[6],
                    )

            case '8':
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    _, created = CsvFile.objects.update_or_create(
                        num=column[0],
                        data=column[1],
                        entity=column[2],
                        entity2=column[3],
                        entity3=column[4],
                        entity4=column[5],
                        entity5=column[6],
                        entity6=column[7],
                    )

            case '9':
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    _, created = CsvFile.objects.update_or_create(
                        num=column[0],
                        data=column[1],
                        entity=column[2],
                        entity2=column[3],
                        entity3=column[4],
                        entity4=column[5],
                        entity5=column[6],
                        entity6=column[7],
                        entity7=column[8],
                    )

        data = CsvFile.objects.all()
        fields = ['num', 'data', 'entity', 'entity2', 'entity3', 'entity4', 'entity5', 'entity6', 'entity7']

        array = []
        for dat in data:
            array.append(dat)

        path = '/Users/aigulusmanova/PycharmProjects/pythonProject/file.csv'
        state_fields = [{"num": 'Num', "data": 'Date', "entity": 'Entity', "entity2": 'Entity2', "entity3": 'Entity3', "entity4": 'Entity4', "entity5": 'Entity5', "entity6": 'Entity6', "entity7": 'Entity7' }]
        with open(path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fields, restval='Unknown', extrasaction='ignore')
            writer.writerows(state_fields)
        for ar in array:
            ar = str(ar)
            ar = ar[0:len(ar)]
            ar = ar.split()
            state_info = [{"num": ar[0], "data": ar[1], "entity": ar[2], "entity2": ar[3], "entity3": ar[4], "entity4": ar[5], "entity5": ar[6], "entity6": ar[7], "entity7": ar[8]}]
            with open(path, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fields, restval='Unknown', extrasaction='ignore')
                writer.writerows(state_info)

        import time
        time.sleep(3)

    if newEntityNum != 'None':
        path = '/Users/aigulusmanova/PycharmProjects/pythonProject/file.csv'
    import numpy as np  # linear algebra
    import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
    import matplotlib.pyplot as plt

    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score

    from pytorch_tabnet.tab_model import TabNetRegressor
    from sklearn.preprocessing import LabelEncoder

    dataForDates = pd.read_csv(path)

    np.random.seed(0)

    columnName = '1'
    match newEntityNum:
        case 'None':
            columnName = 'Entity'
        case 1:
            columnName = 'Num'
        case 3:
            columnName = 'Entity'
        case 4:
            columnName = 'Entity2'
        case 5:
            columnName = 'Entity3'
        case 6:
            columnName = 'Entity4'
        case 7:
            columnName = 'Entity5'
        case 8:
            columnName = 'Entity6'
        case 9:
            columnName = 'Entity7'

    dataColumnName = 'Date'
    columnNameWithoutQuotes = columnName[2:len(columnName)-1]
    print(columnNameWithoutQuotes)
    data = dataForDates.drop(columns=dataColumnName)
    data.Num = data.Num.mask(data.Num.lt(0), 0)
    data.Entity = data.Entity.mask(data.Entity.lt(0), 0)
    data.Entity2 = data.Entity2.mask(data.Entity2.lt(0), 0)
    data.Entity3 = data.Entity3.mask(data.Entity3.lt(0), 0)
    data.Entity4 = data.Entity4.mask(data.Entity4.lt(0), 0)
    data.Entity5 = data.Entity5.mask(data.Entity5.lt(0), 0)
    data.Entity6 = data.Entity6.mask(data.Entity6.lt(0), 0)
    data.Entity7 = data.Entity7.mask(data.Entity7.lt(0), 0)

    dataForDates[dataColumnName] = pd.to_datetime(dataForDates[dataColumnName])
    dataForDates.set_index(dataColumnName, inplace=True)

    # IQR
    # Calculate the upper and lower limits
    Q1 = data[columnName].quantile(0.10)
    Q3 = data[columnName].quantile(0.90)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Create arrays of Boolean values indicating the outlier rows
    upper_array = np.where(data[columnName] >= upper)[0]
    lower_array = np.where(data[columnName] <= lower)[0]

    # Removing the outliers
    data[columnName].drop(index=upper_array, inplace=True)
    data[columnName].drop(index=lower_array, inplace=True)

    data.drop_duplicates()

    data[columnName] = data[columnName].interpolate()  # we will fill the null row

    train = data

    target = columnName
    if "Set" not in train.columns:
        train["Set"] = np.random.choice(["train", "valid", "test"], p=[.8, .1, .1], size=(train.shape[0],))

    train_indices = train[train.Set == "train"].index
    valid_indices = train[train.Set == "valid"].index
    test_indices = train[train.Set == "test"].index
    dataset_name = 'Table'

    categorical_columns = []
    categorical_dims = {}
    for col in train.columns[train.dtypes == object]:
        print(col, train[col].nunique())
        l_enc = LabelEncoder()
        train[col] = train[col].fillna("VV_likely")
        train[col] = l_enc.fit_transform(train[col].values)
        categorical_columns.append(col)
        categorical_dims[col] = len(l_enc.classes_)

    for col in train.columns[train.dtypes == 'float64']:
        train.fillna(train.loc[train_indices, col].mean(), inplace=True)

    unused_feat = ['Set']

    features = [col for col in train.columns if col not in unused_feat + [target]]

    # Список типа int индексов категориальных признаков
    cat_idxs = [i for i, f in enumerate(features) if f in categorical_columns]

    # Список типа int, количество уникальных значений для категориального признака, новые модальности не могут быть предсказаны
    cat_dims = [categorical_dims[f] for i, f in enumerate(features) if f in categorical_columns]

    # Список типа int размеров вложений для каждой категориальной функции (по умолчанию =1)
    # Определение размеров: здесь просто случайный набор
    cat_emb_dim = [5, 4, 3, 6, 2, 2, 9, 10]

    clf = TabNetRegressor(cat_dims=cat_dims, cat_emb_dim=cat_emb_dim, cat_idxs=cat_idxs)

    # np.массив особенностей обучения
    X_train = train[features].values[train_indices]
    # y_train - np.массив учебных целей
    y_train = train[target].values[train_indices].reshape(-1, 1)

    X_valid = train[features].values[valid_indices]
    y_valid = train[target].values[valid_indices].reshape(-1, 1)

    X_test = train[features].values[test_indices]
    y_test = train[target].values[test_indices].reshape(-1, 1)

    # Fitting Random Forest Regression to the dataset
    # import the regressor
    from sklearn.ensemble import RandomForestRegressor

    # create regressor object
    regressor = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=18)

    # fit the regressor with x and y data
    regressor.fit(X_train, y_train)

    RFpreds = regressor.predict(X_test)

    max_epochs = 100 if not os.getenv("CI", False) else 2

    from pytorch_tabnet.augmentations import RegressionSMOTE

    aug = RegressionSMOTE(p=0.2)

    history = clf.fit(
        X_train=X_train, y_train=y_train,
        # Cписок оцениваемых наборов кортежей (X, y)
        eval_set=[(X_train, y_train), (X_valid, y_valid)],
        # Список строковых наборов имен eval
        eval_name=['train', 'valid'],
        # Список показателей оценки
        eval_metric=['rmsle', 'mae', 'rmse', 'mse'],
        max_epochs=50,
        # Количество последовательных периодов без улучшения перед выполнением ранней остановки
        patience=50,
        batch_size=1024, virtual_batch_size=128,
        num_workers=0,
        drop_last=False,
        augmentations=aug,  # aug
    )

    TNpreds = clf.predict(X_test)

    y_true = y_test

    test_score = mean_squared_error(y_pred=TNpreds, y_true=y_true)

    import xgboost as xgb
    from sklearn.model_selection import GridSearchCV

    print("Parameter Optimization")
    xgb_model = xgb.XGBRegressor()
    reg_xgb = GridSearchCV(xgb_model,
                           {'max_depth': [3, 5, 7],
                            'n_estimators': [50, 100, 200]}, verbose=1)
    reg_xgb.fit(X_train, y_train)
    print(reg_xgb.best_score_)
    print(reg_xgb.best_params_)

    XGBpreds = reg_xgb.predict(X_test)

    from catboost import CatBoostRegressor

    # Initialize CatBoostRegressor
    model = CatBoostRegressor(iterations=2,
                              learning_rate=1,
                              depth=3,
                              )
    # Fit model
    ctb = model.fit(X_train, y_train)
    # Get predictions
    CTBpreds = ctb.predict(X_test)

    # second feature matrix
    RFpreds = np.asanyarray(RFpreds)
    RFpreds = RFpreds.reshape(-1, 1)
    TNpreds = np.asanyarray(TNpreds)
    TNpreds = TNpreds.reshape(-1, 1)
    XGBpreds = np.asanyarray(XGBpreds)
    XGBpreds = XGBpreds.reshape(-1, 1)
    CTBpreds = np.asanyarray(CTBpreds)
    CTBpreds = CTBpreds.reshape(-1, 1)

    X_train2 = pd.DataFrame({'RF': RFpreds.flatten(),
                             'TN': TNpreds.flatten(),
                             'XGB': XGBpreds.flatten(),
                             'CTB': CTBpreds.flatten(),
                             })

    # second-feature modeling using linear regression
    from sklearn import linear_model

    reg = linear_model.LinearRegression()
    reg.fit(X_train2, y_test)

    # prediction using the test set
    X_test2 = pd.DataFrame({'RF': RFpreds.flatten(),
                            'TN': TNpreds.flatten(),
                            'XGB': XGBpreds.flatten(),
                            'CTB': CTBpreds.flatten(),
                            })

    # Non-log scale
    y_pred = reg.predict(X_test2)

    score = r2_score(y_true, y_pred)
    accuracy = "Точность модели составляет {}%".format(round(score, 2) * 100)
    print(accuracy)

    y_pred = np.asanyarray(y_pred)
    y_pred = y_pred.reshape(-1, 1)
    submission = pd.DataFrame({
        # "Id": test_ID,
        "Data": y_pred.flatten()
    })

    test = pd.DataFrame(y_test, columns=['Actual'])
    pred = pd.DataFrame(y_pred, columns=['Predict'])

    timestep = 120


    def insert_end(Xin, new_input):
        # print ('Before: \n', Xin , new_input )
        for i in range(timestep - 1):
            Xin[i] = Xin[i + 1]
        Xin[timestep - 1] = new_input
        # print ('After :\n', Xin)
        return Xin


    from datetime import timedelta

    future = timestep
    forcast = []
    Xin = X_test2
    Xin = np.asanyarray(Xin)
    print(Xin)
    time = []
    for i in range(future):
        out = reg.predict(Xin)
        forcast.append(out[0, 0])
        print(forcast)
        Xin = insert_end(Xin, out[0, 0])
        time.append(pd.to_datetime(dataForDates.index[-1]) + timedelta(days=i + 1))

    forcasted_output = np.asanyarray(forcast)
    forcasted_output = forcasted_output.reshape(-1, 1)

    forcasted_output = pd.DataFrame(forcasted_output)
    date = pd.DataFrame(time)
    df_result = pd.concat([date, forcasted_output], axis=1)
    df_result.columns = "Date", "Forecasted"

    if newEntityNum == 'None':
        photoPath = '/Users/aigulusmanova/PycharmProjects/pythonProject/vkr/main/static/main/img/saved_image.png'
    else:
        photoPath = '/Users/aigulusmanova/PycharmProjects/pythonProject/vkr/main/static/main/img/saved_image1.png'

    import matplotlib
    matplotlib.use('agg')
    plt.figure(figsize=(16, 8))
    plt.title('Prediction')
    plt.xlabel('Дата', fontsize=18)
    plt.ylabel('Прогнозируемое значение', fontsize=18)
    plt.plot(df_result.set_index('Date')[['Forecasted']], "r--")
    plt.savefig(photoPath)

    from PIL import Image

    im = Image.open(photoPath)
    im_crop = im.crop((112, 50, 1470, 775))
    im_crop.save(photoPath, quality=95)
    cache.clear()

    return accuracy


def file_upload(request):
    if request.method == 'GET':
        return render(request, 'main/second.html')

    # ColumnsCount.objects.all().delete()

    count = CsvFile.objects.all()[:1]
    count = str(count)
    length = len(count)
    length = int(length)
    if length != 13:
        CsvFile.objects.all().delete()
        os.remove('/Users/aigulusmanova/PycharmProjects/pythonProject/file.csv')

    FieldName.objects.all().delete()

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.scv'):
        messages.error(request, 'Это не csv файл.')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    func = model(io_string)
    accuracy = func

    ColumnsCount.objects.all().delete()

    import random
    number = random.randint(204355, 35454555)

    return render(request, 'main/second.html', {'number': number, 'accuracy': accuracy})


def delete(request):
    if request.method == 'POST':
        ColumnsCount.objects.all().delete()

        count = CsvFile.objects.all()[:1]
        count = str(count)
        length = len(count)
        length = int(length)
        if length != 13:
            CsvFile.objects.all().delete()
            os.remove('/Users/aigulusmanova/PycharmProjects/pythonProject/file.csv')

        FieldName.objects.all().delete()
        return redirect('home')

    return render(request, 'main/delete.html')


def otherForecasts(request):
    data = {
        'title': 'Прогноз на другие сущности',
    }
    if request.method == 'POST':
        form2 = FieldForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('otherForecasts')

    form2 = FieldForm()

    return render(request, 'main/other.html', {'form2': form2, 'data': data})


def otherForecast(request):
    data = {
        'title': 'Прогноз',
    }

    io_string = 0
    func = model(io_string)

    accuracy = func

    return render(request, 'main/otherForecast.html', {'data': data, 'accuracy': accuracy})