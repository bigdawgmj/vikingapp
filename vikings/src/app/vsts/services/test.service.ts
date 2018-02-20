import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';

import { Teammate } from '../model/teammate';

@Injectable()
export class TestService {
  private baseUrl = 'api/team';

  constructor(private http: HttpClient) { }

  getTeam(): Observable<Teammate[]> {
    return this.http.get<Teammate[]>(this.baseUrl);
  }

  addMember(mate: Teammate): Observable<any> {
    return this.http.post<any>(this.baseUrl + '/member', mate);
  }

}