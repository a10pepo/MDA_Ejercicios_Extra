FROM alpine
RUN mkdir Carpeta_ejercicio
WORKDIR /Carpeta_ejercicio
COPY Init_script.sh Carpeta_ejercicio/Init_script.sh
RUN echo "Ejercicio 1" > Carpeta_ejercicio/Ejercicio_1.txt
RUN apk update && apk add bash
RUN chmod +x Carpeta_ejercicio/Init_script.sh
ENTRYPOINT ["Carpeta_ejercicio/Init_script.sh"]