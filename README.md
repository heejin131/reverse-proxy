# reverse-proxy
- 성능
- 부하분산(LB)
- 가상호스트 및 라우팅

## Python server
```bash
$ python -m http.server --directory pyweb1 8001
$ python -m http.server --directory pyweb2 8002
$ python -m http.server --directory blog 8003
```

## nginx
- https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview
```bash
# install
$ sudo apt install nginx

$ sudo service nginx restart
$ sudo service nginx stop
$ sudo service nginx start
$ sudo service nginx status #-> worker 16ea
$ sudo nginx -t #테스트
```

## nGrinder
- http://localhost:8000 (admin/admin)

```bash
$pwd
~/app
$ sudo apt install openjdk-11-jdk #java
$tree - L 2
.
├── ngrinder-agent
│   ├── lib
│   ├── run_agent.bat
│   ├── run_agent.sh
│   ├── run_agent_bg.sh
│   ├── run_agent_internal.bat
│   ├── run_agent_internal.sh
│   ├── stop_agent.bat
│   └── stop_agent.sh
└── ngrinder-controller
    └── ngrinder-controller-3.5.9-p1.war

# controller
$ sudo apt install openjdk-11-jdk
$ wget https://github.com/naver/ngrinder/releases/download/ngrinder-3.5.9-p1-20240613/ngrinder-controller-3.5.9-p1.war

$ java - jar ngrinder-controller-3.5.9-p1.war

# agent
$ ./run_agent.sh
```

## netstat
```bash
sudo apt update
sudo apt install net-tools
```

## docker
```bash
$ docker compose up -d  # 백그라운드에서 컨테이너 실행
$ docker compose down   # 컨테이너 중지 및 네트워크 제거
$ docker compose stop   # 컨테이너 중지
$ docker compose start  # 중지된 컨테이너 다시 시작
$ docker compose restart  # 컨테이너 재시작
$ docker compose down  # 컨테이너, 네트워크 제거
$ sudo docker compose stats # 성능 모니터링

# scale out
$ sudo docker compose up -d --scale web1=3
```

## nginx 
```bash
$ sudo docker exec -it <LB_NAME> bash
$ nginx -s reload

```

## FastAPI
```bash
# Ref
https://fastapi.tiangolo.com

$ fastapi dev main.py
```

## PDM to requirements.txt
```bash
$ pdm export -o requirements.txt --without-hashes
```
