# install

brew install postgresql@15

brew info postgresql@15

##echo 'export PATH="/usr/local/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc


brew services start postgresql@15
brew services stop postgresql@15

createuser -s postgres
psql -U postgres -h localhost

## pgadmin4

