🎯 Probar el Listener

🔹 Entrada:

for (i = 0; i < 3; i = i + 1) {
    x = x + 2;
};

🔹 Salida esperada:

Inicialización detectada: i=0
Condición detectada: i<3
Actualización detectada: i=i+1
Asignación detectada: x=x+2;
Se ha detectado un ciclo for.

🛠️ Probar test_visitor.py

🔹 Entrada:

Ingresa código: for (i = 0; i < 3; i = i + 1) { x = x + 2; };

🔹 Salida esperada:
Asignación: x = 2
Asignación: x = 4
Asignación: x = 6