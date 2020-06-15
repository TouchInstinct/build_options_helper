# Build Options Helper (BOH)

An utility to work with build options.

Can generate:

- iOS configs in json format
- [Teamcity web parameters](https://github.com/grundic/teamcity-web-parameters)

## Usage

```
usage: helper.py [-h] --build-parameters-path BUILD_PARAMETERS_PATH
                 --output-folder OUTPUT_FOLDER --render
                 {ios_build_settings,team_city_web_parameters} --platform
                 {ios,android}

optional arguments:
  -h, --help            show this help message and exit
  --build-parameters-path BUILD_PARAMETERS_PATH, -bp BUILD_PARAMETERS_PATH
                        Relative or absolute path to build parameters in yaml
                        format.
  --output-folder OUTPUT_FOLDER, -o OUTPUT_FOLDER
                        Path to writeable directory for execution results.
  --render {ios_build_settings,team_city_web_parameters}, -r {ios_build_settings,team_city_web_parameters}
                        Task that should be done.
  --platform {ios,android}, -p {ios,android}
                        Platform for which build parameters rules should be
                        applied.
```