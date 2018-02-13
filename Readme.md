# Test RPM Build repo

This repo was created to host a test project, for building an RPM using Jenkins. The `_template` dir is just to store what a default template from `rpmdev-newspec` outputs.


The `test_build.sh` was created so that it can be called by Jenkins, to build our test RPM.  The files in the repo are not doing much, but services as a base for create other RPMS.

Also, the spec file (`test_rpm.spec`) is utilizing very little of a spec file's power, but it gets the job done.

To test usage this repo

* Spin up a Jenkins Instance, like in your vagrant set.
* Ensure RPMs are installed
   * rpm-build
   * rpmdevtools  (Optional)
   * rpm-build  (Optional)
   * rpmlint  (Optional)

* Within Jenkins:
   * Setup a _FreeStype_ Project
   * Enable GIthub Project. Point it to this Git Repo
   * Under `Build`
      * Set `Execute shell` to Command `$WORKSPACE/test_build.sh`
   * Under Post-build Action
      * Archive the artifact, set Files to archive to `RPMS/x86_64/*`