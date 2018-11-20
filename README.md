# CPS 592 - TankSoar Project
Project consists of a modified TankSoar project taken from [here](#https://github.com/SoarGroup/Domains-Eaters-TankSoar). Additionally, sample templates are written in Java and Python to communicated with SOAR using SML. Python also contains a set of tools to generate Graphviz dot graphs as `.png` files from printed states from any SOAR Debugger tools. A python command-line debugger is also in the python toolset.

Sample TankSoar configuration files are stored in `tanksoar_configs/` as `.cnf` files and are used for the project.

The modified TankSoar in this project implements the following:
|Feature  |Description  |
|:--|:--|
|Teams  |Tanks are on teams of either 0 or 1 which alternate as tanks are added.  |
|Logger	|A logger is used to output results and stats |
|Configuration Files| Configuration to run TankSoar headless and with multiple runs |

## Feature Descriptions
### Teams
Tanks are on teams of either 0 or 1 which alternate as tanks are added. Soar productions are able to query this through the IO link to determine which team the tank is on. The setup of the current tank's team is setup as `[Input-Link] --> Team --> Value`. Additionally, radar now has the capability to scan for the detected tank's team which is setup as `[Input-Link] --> Radar --> Tank --> Team --> Value`. A graphed detailed description can be [found below](#graph).

### Logger
A log file is generated at the project root named `tanksoar.log` which outputs the run counter and the tank stats for each tank per run.

## Setup
A `.jar` file is precompiled and should run in conjunction with the SOAR tutorials. Since the `jar` file relies on external SOAR libraries, the quickest way to use the precompiled `.jar` file is to replace the file stored at the tutorial's jar file `bin/Eaters_TankSoar.jar` with the precompiled file at `Java/Domains-Eaters-TankSoar/Eaters_TankSoar.jar`. Simply running the tutorial's `TankSoar.bat` at this point will launch the modified TankSoar project.

## Configuration
To load a configuration such as the `tanksoar_configs/tanksoar.cnf` configuration, edit the `TankSoar.bat` file and replace in the script the `cnf` file to point to the Project's new configuration. The default is set to `bin\games\tanksoar.cnf`, be careful about the backslashes when working with windows.

## Configuration Settings
The current configuration found in `tanksoar_configs/tanksoar.cnf` is as follows:

	# define game
	general.game = "tanksoar";
	general.map = "bin/games/maps/tanksoar/default.txt";
	general.runs = 200;
	general.headless = true;

	soar.spawn_debuggers = false;

	# define players
	players.active_players = [ "tank1", "tank2", "tank3", "tank4" ];
	players.tank1.productions = "test_soar/simple-bot.soar";
	players.tank2.productions = "test_soar/simple-bot.soar";
	players.tank3.productions = "test_soar/simple-bot.soar";
	players.tank4.productions = "test_soar/simple-bot.soar";

	# define winning score condition
	terminals.winning_score = 50;

Modify the file to point to the correct SOAR files to be used for their respective tanks.

## Python Tools
To use some of the python tools, required packages need to be installed before they can be used. The required packages are listed in `requirements.txt` and can be installed using the `pip` tool by running `pip install -r requirements.txt` or `python -m pip install requirements.txt`.
|Tool|Description  |
|:--|:--|
|`state2dot.py`|Parse state output into graph plot  |

# <a name="graph"></a>`state2dot.py`
To get a state output, run the SOAR debugger and print out the state (ex: `print S1 --depth`) and copy/paste the output to a file. Run the tool using `python state2dot.py sample_s1_output` to generate an output graph image. The generated image is named `output.png`. An example can be seen below. The example below also demonstrates the sample output using the modified TankSoar project with teams implemented which can be seen at the input link and at the tank's radar when detecting another tank.
![Sample SOAR Graph](https://github.com/Kanaderu/CPS-592_TankSoar_Project/raw/master/Python/output.png)
