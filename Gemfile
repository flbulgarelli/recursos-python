source "https://rubygems.org"

gem "github-pages", "~> 217", group: :jekyll_plugins

gem "jekyll-theme-minimal", "~> 0.2"

install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end
gem "wdm", "~> 0.1.0", :install_if => Gem.win_platform?
gem "kramdown-parser-gfm"
