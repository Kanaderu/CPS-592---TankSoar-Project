
set SOAR_HOME=%~dp0bin
set PATH=%SOAR_HOME%;%PATH%

start javaw -Djava.library.path=%SOAR_HOME% -jar bin\Eaters_TankSoar.jar tanksoar_fallacyfallacy_test.cnf
#start javaw -Djava.library.path=%SOAR_HOME% -jar bin\Eaters_TankSoar.jar tanksoar_selfmotivated_test.cnf