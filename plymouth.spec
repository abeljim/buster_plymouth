Name:       {{{ git_dir_name }}}

# git_dir_version returns version based on commit and tag history of the Git project
Version:    {{{ git_dir_version }}}

# This can be useful later for adding downstream patches
Release:    1%{?dist}

# Basic description of the package
Summary:    Buster Plymouth package.

# License. Hopefully free or at least open-source. We assume GPLv2+ here.
License:    GPLv2+

# Home page of the project. Can also point to the public Git repository page.
URL:        https://github.com/abeljim/buster_plymouth.git

# Detailed information about the source Git repository and the source commit
# for the created rpm package
VCS:        {{{ git_dir_vcs }}}

# git_dir_pack macro places the repository content (the source files) into a tarball
# and returns its filename. The tarball will be used to build the rpm.
Source:     {{{ git_dir_pack }}}

# More detailed description of the package
%description
Plymouth for Buster.

# The following four sections already describe the rpm build process itself.
# prep will extract the tarball defined as Source above and descend into it.
%prep
{{{ git_dir_setup_macro }}}

# This will invoke `make` command in the directory with the extracted sources.
%build

# This will copy the files generated by the `make` command above into
# the installable rpm package.
%install
make install

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
/usr/share/plymouth/themes/buster

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}
