$rootDir = (get-item $PSScriptRoot).Parent.FullName
pytest --cov=bowling "$($rootDir)\src\tests" --cov-report term-missing
