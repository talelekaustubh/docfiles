require 'sinatra'

set :bind, '0.0.0.0'

get '/' do
  "Hello from Krishna IWith Ruby in Docker!"
end