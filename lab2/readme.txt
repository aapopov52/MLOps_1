#Некорые пояснения по коду на Джанкинс


#!/bin/bash
DIR_BUILD="$WORKSPACE"
# создаём рабочую папку Джанкенс (если её нет)
mkdir $WORKSPACE
# Копируем всё из нашего открытого репозитория
git clone https://github.com/aapopov52/MLOps_1.git

# копируем весь код по первому проекту из папочки 1 в основную (рабочую) диркторию Джанкенса
cp $DIR_BUILD/MLOps_1/lab1/* $DIR_BUILD/

# удаляем о, чо загрузили с ГитХаба
sudo rm -r $DIR_BUILD/MLOps_1
# Стандартная процедура установки вирт среды, включения вирт среды, установки ненобходимых модулей
python3 -m venv "$DIR_BUILD/env"

source "$DIR_BUILD/bin/activate"

python3 -m pip install --upgrade pip
pip install -r "$DIR_BUILD/requirements.txt"

# запускаем все питоновские файлики из ранее созданного скрипта
bash "$DIR_BUILD/pipeline.sh"

# радостно сообщаем, что всё отработано
echo "отработал"
