class Mansplain < Formula
  include Language::Python::Virtualenv
  desc "Basically it explains stuff to you"
  homepage ""
  url "https://github.com/emdoyle/homebrew-mansplain/raw/master/mansplain.tar.gz"
  sha256 "d88c1c67e1a097c0ff1bf5f645e78cdc1af060236efdd5d48071a785941e33c7"
  version "1"

  depends_on "python"

  def install
    virtualenv_install_with_resources
  end
end
