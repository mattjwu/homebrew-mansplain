class Mansplain < Formula
  include Language::Python::Virtualenv
  desc "Basically it explains stuff to you"
  homepage ""
  url "https://github.com/emdoyle/homebrew-mansplain/raw/master/mansplain.tar.gz"
  sha256 "13bd3ff930734d0ab5554791fb97c43de3774231beb68716b60c742e8bfaeb13"
  version "1"

  depends_on "python"

  def install
    virtualenv_install_with_resources
  end
end
