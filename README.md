# Сборка и запуск
git clone https://github.com/kirillyasnov/deposit_calculator.git \
docker build -t sber_test . \
docker run sber_test -p 80:80 
