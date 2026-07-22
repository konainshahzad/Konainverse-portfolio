echo "BUILD START"
python3 -m pip install --upgrade pip
python3 -m pip install --user -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"