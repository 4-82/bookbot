{
  description = "";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: let
    systems = ["x86_64-linux" "aarch64-linux" ];
    all = nixpkgs.lib.genAttrs systems;
 in  {

    devShells = all (sys: let
      pkgs = nixpkgs.legacyPackages.${sys};
    in {
      default = pkgs.mkShell {
        packages = builtins.attrValues {inherit (pkgs) nil git gh bootdev-cli ripgrep python3;
        inherit (pkgs.python313Packages) python-lsp-server;
      };
      };
     });          
  };
}
