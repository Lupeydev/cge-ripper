{ stdenv, fetchurl, makeWrapper }:

stdenv.mkDerivation rec {
  pname = "directmap";
  version = "1.0";

  src = fetchurl {
    url = "https://github.com/Lupeydev/cge-ripper/releases/download/Main/directmap";
    sha256 = "19mqybx91sh08i11vsvxwnr5kivcm1jhf1zgm740v64bfqqp19ga";
  };

  nativeBuildInputs = [ makeWrapper ];

  installPhase = ''
    mkdir -p $out/bin
    cp directmap $out/bin/
    wrapProgram $out/bin/directmap --prefix LD_LIBRARY_PATH : ${stdenv.lib.makeLibraryPath [ stdenv.cc.cc stdenv.cc.libc ]}
  '';

  meta = with stdenv.lib; {
    description = "CGE-193 ARG Map Downloader ANOMIDAE";
    license = stdenv.lib.licenses.mit;
    maintainers = with stdenv.lib.maintainers; [ lupeydev ];
  };
}
