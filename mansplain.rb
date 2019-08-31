class Mansplain < Formula
  include Language::Python::Virtualenv
  desc "Basically it explains stuff to you"
  homepage ""
  url "https://github.com/emdoyle/homebrew-mansplain/raw/master/mansplain.tar.gz"
  sha256 "35585a14876386089b9b8ef43393511aa57cddb0310791a7a44439b0846f7392"
  version "1"

  depends_on "python"

  def install
    virtualenv_install_with_resources
  end
end
