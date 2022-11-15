$rootDir = (get-item $PSScriptRoot).Parent.FullName
pytest --cov=bowling "$($rootDir)\tests" --cov-report term-missing
