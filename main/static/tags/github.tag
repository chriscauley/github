<repository-viewer>
  <div class="row">
    <div class="col-sm-4">
      <p>Click any of these to toggle them from the chart to the right</p>
      <div each={ user_list } class="btn btn-block btn-{ checked?'success':'default' }" onclick={ parent.toggle }>
        <span class="udot c{ colorClass }"></span>
        { username } ({ repositories.length })
      </div>
    </div>
    <div class="col-sm-8">
      <center>
        Y axis is stars, X axis is watchers, size is forks.
        <br>
        Hover over dot for details.
      </center>
      <div class="github-plot" data-max_stars={ max_stars } data-max_watchers={ max_watchers }>
        <div each={ user_list } if={ checked }>
          <div class="dot { className }" each={ repositories } style="bottom: { b }%; left: { l }%;"
               title="{ username }/{ reponame } { stars }&#x2605; { watchers }&#128065; { forks }Y"></div>
        </div>
      </div>
    </div>
  </div>

  var that = this;
  this._users = {}, this.user_list = [], this._usernames = [];
  this.opts.repositories.forEach(function(repo) {
    var username = repo.username;
    if (!that._users[username]) {
      that._usernames.push(username)
      that._users[username] = {
        username: username,
        repositories: [],
        checked: true,
        colorClass: that._usernames.indexOf(username)%8,
      }
      that.user_list.push(that._users[username]);
    }
    that._users[username].repositories.push(repo);
  });

  toggle(e) {
    e.item.checked = !e.item.checked;
  }

  this.on("update", function() {
    var fields = ['stars','watchers','forks'];

    // create empty arrays
    fields.forEach(function(f) { that[f] = []; })

    // get each value for each array
    this.opts.repositories.forEach(function(repo) {
      if (!that._users[repo.username].checked) { return }
      fields.forEach(function (f) { that[f].push(repo[f]); });
    });

    // calculate max for each field
    fields.forEach(function(f) {
      that["max_"+f] = Math.max.apply(this,that[f]);
    });

    // and now the css for each repo
    this.opts.repositories.forEach(function(repo) {
      repo.b = repo.stars/that.max_stars*100;
      repo.l = repo.watchers/that.max_watchers*100;
      if (repo.forks > 100) { repo.className = "s5" }
      else if (repo.forks > 50) { repo.className = "s4" }
      else if (repo.forks > 20) { repo.className = "s3" }
      else if (repo.forks > 10) { repo.className = "s2" }
      else if (repo.forks > 5) { repo.className = "s1" }
      else { repo.className = "s0" }

      // I can't actually color :(
      repo.className += " c"+ (that._usernames.indexOf(repo.username)%8);
    })
  });
</repository-viewer>
